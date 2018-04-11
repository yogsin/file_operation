# 文件操作

#include "unistd.h"
#include <fstream>
#include "sys/stat.h"
#include <dirent.h>
#include "boost/filesystem/operations.hpp"
#include "boost/filesystem/path.hpp"

//traversal files
void traversal_allfiles_(const std::string rootPath, const std::string current, std::vector<std::string> &ansVec) {
  DIR *dir;
  struct dirent *ptr;
  if ((dir = opendir(current.c_str())) == NULL) {
    return;
  }
  while ((ptr = readdir(dir)) != NULL) {
    std::string name = ptr->d_name;
    if (name.length() == 1 && name.at(0) == '.') continue;
    if (name.length() == 2 && name.at(0) == '.') continue;
    struct stat info;
    stat((current + name).c_str(), &info);
    if (S_ISDIR(info.st_mode)) {
      name = current + name + "/";
      traversal_allfiles_(rootPath, name, ansVec);
    } else {
      name = current.substr(rootPath.length(), current.length() - rootPath.length()) + name;
      int qpos = name.find_last_of(' ');
      if (qpos == -1) {
        ansVec.push_back(name);
      }
    }
  }
  closedir(dir);
}
void traversal_allfiles(const std::string rootPath, std::vector<std::string> &ansVec) {
  traversal_allfiles_(rootPath, rootPath, ansVec);
}
void traversal_alldirs_(const std::string rootPath, const std::string current, std::vector<std::string> &ansVec) {
  DIR *dir;
  struct dirent *ptr;
  if ((dir = opendir(current.c_str())) == NULL) return;
  while ((ptr = readdir(dir)) != NULL) {
    std::string name = ptr->d_name;
    if (name.length() == 1 && name.at(0) == '.') continue;
    if (name.length() == 2 && name.at(0) == '.') continue;
    struct stat info;
    stat((current + name).c_str(), &info);
    if (S_ISDIR(info.st_mode)) {
      std::string toPush = current.substr(rootPath.length(), current.length() - rootPath.length()) + name + '/';
      ansVec.push_back(toPush);
      traversal_alldirs_(rootPath, (rootPath + toPush), ansVec);
    }
  }
  closedir(dir);
}
void traversal_alldirs(const std::string rootPath, std::vector<std::string> &ansVec) {
  traversal_alldirs_(rootPath, rootPath, ansVec);
}
void traversal_single_files(const std::string rootPath, std::vector<std::string> &ansVec) {
  DIR *dir;
  struct dirent *ptr;
  if ((dir = opendir(rootPath.c_str())) == NULL) return;
  while ((ptr = readdir(dir)) != NULL) {
    std::string name = ptr->d_name;
    if (name.length() == 1 && name.at(0) == '.') continue;
    if (name.length() == 2 && name.at(0) == '.') continue;
    struct stat info;
    stat((rootPath + name).c_str(), &info);
    if (!S_ISDIR(info.st_mode)) {
      int qpos = name.find_last_of(' ');
      if (qpos == -1) {
        ansVec.push_back(name);
      }
    }
  }
  closedir(dir);
}
void traversal_single_dirs(const std::string rootPath, std::vector<std::string> &ansVec) {
  DIR *dir;
  struct dirent *ptr;
  if ((dir = opendir(rootPath.c_str())) == NULL) return;
  while ((ptr = readdir(dir)) != NULL) {
    std::string name = ptr->d_name;
    if (name.length() == 1 && name.at(0) == '.') continue;
    if (name.length() == 2 && name.at(0) == '.') continue;
    struct stat info;
    stat((rootPath + name).c_str(), &info);
    if (S_ISDIR(info.st_mode)) {
      name += "/";
      ansVec.push_back(name);
    }
  }
  closedir(dir);
}
void traversalMakeDir(const std::string dirs) {
  int qpos1 = -1;
  int qpos2 = -1;
  std::string name = dirs;
  std::string toMake = "/";
  while (true) {
    if (name.length() <= 1) break;
    qpos1 = name.find_first_of('/') + 1;
    name = name.substr(qpos1, name.length() - qpos1);
    qpos2 = name.find_first_of('/');
    toMake += name.substr(0, qpos2) + '/';
    name = name.substr(qpos2, name.length() - qpos2);
    if (-1 == access(toMake.c_str(), F_OK)) {
      mkdir(toMake.c_str(), S_IWRITE);
    }
  }
}

//string utils
std::string getFileFolder(const std::string abs_fileName) {
  int qpos1 = abs_fileName.find_last_of('/');
  return abs_fileName.substr(0, qpos1 + 1);
}
std::string getFileName(const std::string abs_fileName, bool includeExt) {
  int qpos1 = abs_fileName.find_last_of('/');
  int qpos2 = abs_fileName.find_last_of('.');
  if (includeExt) return abs_fileName.substr(qpos1 + 1, abs_fileName.length() - qpos1);
  return abs_fileName.substr(qpos1 + 1, qpos2 - qpos1 - 1);
}
std::string addIdNum(const std::string abs_fileName, const int id) {
  int qpos = abs_fileName.find_last_of('.');
  std::string ext = abs_fileName.substr(qpos, abs_fileName.length() - qpos);
  char t[256];
  sprintf(t, "%s_%d%s", abs_fileName.substr(0, qpos).c_str(), id, ext.c_str());
  return t;
}
