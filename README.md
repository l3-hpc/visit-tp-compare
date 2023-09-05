# visit-tp-compare

Get the repo
```
git clone https://github.com/l3-hpc/visit-tp-compare.git
cd visit-tp-compare
```

Get the sample data, untar.
```
wget https://renc.osn.xsede.org/ees210015-bucket01/outputs_shiny-le.tar
tar -xvf outputs_shiny-le.tar
```

It's pretty clunky, just uncomment and comment out stuff, then do
```
visit -cli -nowin -s movie_loop.py
```

Then modify ffmpeg.sh and do `source ffmpeg.sh`, or just modify and paste the command:
```
ffmpeg -framerate 15 -i TP_nosinkout_layer1_%04d.png TP_sinkout_layer1.mp4
```
