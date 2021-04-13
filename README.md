# Test dataset creator for git benchmarking

## Usage

Copy `config.py.sample` to `config.py`, then edit it:

`output_dir`: path to directory with two datasets (dataset `./a/` - many subdirectories, dataset `./b/` - standard “flat” directories scheme).

`files_per_lng`: number of files per each language  (by default we use 23; languages list specified at `tld` variable).

After that you can run `python3 create.py` to create this datasets. To compare time of some git opeations under *nix you can use `bench.sh`. 
For example we got this values on Linux extfs4 with git v.2.17.1:


 *subdirs*# `git add -A`


 real	0m4,904s

 user	0m2,410s

 sys	0m2,385s


 *flat*# `git add -A`


 real	0m3,223s

 user	0m1,738s

 sys	0m1,474s

---

 *subdirs*# `commit`:


 real	0m5,734s

 user	0m1,946s

 sys	0m3,635s


 *flat*# `commit`:


 real	0m0,859s

 user	0m0,371s

 sys	0m0,295s

---

 *subdirs*# `git status`


 real	0m1,599s

 user	0m0,647s

 sys	0m0,798s


 *flat*# `git status`

 real	0m1,028s

 user	0m0,215s

 sys	0m0,306s

