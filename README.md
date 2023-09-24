#!/bin/bash
sudo su
dnf install git -y
git clone https://github.com/KelvinSing/internshipAPP.git
cd internshipAPP
dnf install python-pip -y
pip3 install flask pymysql boto3
python3 InternshipAPP.py
