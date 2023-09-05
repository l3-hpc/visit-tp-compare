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

The file ***movie_loop_script.py*** takes command line arguments to make the plot.  It assumes the file structure of the shiny outputs.  (You can change it.)

The following will make one movie:
```
visit -cli -nowin -s movie_loop_script.py which_db which_plot do_rm istates
```

`which_db` defines the FVCOM file and the corresponding timestamp.
- 0 = no sink out
- 1 = sink out
- 2 = leem (TP=sum of TP terms)

`which_plot` determines which session file to use
- layer1 = top view, first layer
- layer19 = top view, last layer
- 3D = 3D side view
- 3Dslice = 3D with three-slice operator

Set `do_rm` = rm if you want to delete the intermediate pngs.  (It will not delete them if it is anything else.)

`istates` is the number of frames (minus one, because Python does that).  If istates=0, it will make an image for every timestep.

  
For example, this makes a movie of TP for all timesteps, with no sinking out, top view of first layer, removes the intermediate pngs.
```
visit -cli -nowin -s movie_loop_script.py 0 layer1 rm 0
```

The command line argument version allows you to make a script by pasting commands in a file.  (You can use ser2par or launch to parallelize it.)

This does all of the things:
```
source all_movies.sh
```

Do a test first, with just 5 frames:
```
source short_movies.sh
```

The problem with the above is that there is no error checking, and if VisIt breaks on a step, it will not move to the next command.  Just test it with small number of istates before running a big job. 






