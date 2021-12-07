#!/bin/bash
file_exist(){
  if [ -f "$1" ];then
    printf "file %s exists, continuing\\n" "$1"
  else
    printf "file not exist, exiting\\n"
    exit
  fi
}
folder_exist(){
  if [ -d "$1" ];then
    printf "folder %s exists, continuing\\n" "$1"
  else
    printf "folder not exist, exiting\\n"
    exit
  fi
}
