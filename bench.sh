#!/bin/sh

this_dir=`pwd`
dataset_dir="${this_dir}/../test-dataset"

cd "${dataset_dir}"

cd "${dataset_dir}/a"
echo "Variant A, time, 'git init':"
pwd
time git init
echo "\n"
echo "Variant A, time, 'git add -A'"
time git add -A
echo "Variant A, time, 'git commit':"
time git commit -q -m 'test commit'

echo "\n"

cd "${dataset_dir}/b"
echo "Variant B, time, 'git init':"
pwd
time git init
echo "\n"
echo "Variant B, time, 'git add -A':"
time git add -A
echo "\n"
echo "Variant B, time, 'git commit':"
time git commit -q -m 'test commit'


#git & cat /proc/$!/io