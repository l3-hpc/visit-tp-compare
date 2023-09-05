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

## Basic loop

This is meant to be really easy to read: just uncomment and comment out stuff, then do
```
visit -cli -nowin -s movie_loop.py
```

Then modify ffmpeg.sh and do `source ffmpeg.sh`, or just modify and paste the command:
```
ffmpeg -framerate 15 -i TP_nosinkout_layer1_%04d.png TP_nosinkout_layer1.mp4
```
That ffmpeg command should work everywhere, but it doesn't encode properly for many movie applications.  They open in Google Chrome.

Then move or remove pngs.
```
rm *.png
```

## Script loop
This does all of the things.






