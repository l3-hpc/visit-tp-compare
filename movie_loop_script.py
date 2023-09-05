#Calendar
import datetime
import calendar
import sys
import subprocess

#Argument is array number for plot variable 
which_db = int(sys.argv[1])
which_plot = sys.argv[2]
do_rm = sys.argv[3]
istates = int(sys.argv[4])

#Choose dataset and timestamp modifier
if which_db == 0:
    db = "outputs_shiny-le/output_nosinkout/leem_0001.nc"
    t_start = calendar.timegm(datetime.datetime(1858, 11, 17, 0, 0, 0).timetuple())
    BASE_FILENAME = "TP_nosinkout_"
elif which_db == 1:
    db = "outputs_shiny-le/output_sinkout/leem_0001.nc"
    t_start = calendar.timegm(datetime.datetime(1858, 11, 17, 0, 0, 0).timetuple())
    BASE_FILENAME = "TP_sinkout_"
elif which_db == 2:
    db = "outputs_shiny-le/output_leem/TP_crop.nc"
    t_start = calendar.timegm(datetime.datetime(2013, 3, 1, 0, 0, 0).timetuple())
    BASE_FILENAME = "TP_leem_"

#Restore a session file
if which_plot == 'layer1':
    RestoreSessionWithDifferentSources("tp_layer1.session", 0, db)
    BASE_FILENAME = BASE_FILENAME + "layer1_"
elif which_plot == 'layer19':
    RestoreSessionWithDifferentSources("tp_layer19.session", 0, db)
    BASE_FILENAME = BASE_FILENAME + "layer19_"
elif which_plot == '3D':
    RestoreSessionWithDifferentSources("tp_3D.session", 0, db)
    BASE_FILENAME = BASE_FILENAME + "3D_"
elif which_plot == '3Dslice':
    RestoreSessionWithDifferentSources("tp_3D_slice.session", 0, db)
    BASE_FILENAME = BASE_FILENAME + "3Dslice_"

print(BASE_FILENAME)
print(db)
#sys.exit()

#Create a time slider
slider = CreateAnnotationObject("TimeSlider")
slider.text = ""
slider.height = 0.05
slider.width = 0.3
slider.position = (0.03, 0.94)
m = GetMetaData(db)

if istates == 0:
    nstates = TimeSliderGetNStates()
else:
    nstates = min(istates,TimeSliderGetNStates())

for state in range(nstates): 
#for state in range(6):
    SetTimeSliderState(state)
    tcur = m.times[state]*86400. + t_start
    ts = datetime.datetime.utcfromtimestamp(tcur).strftime('%Y-%m-%d %H:%M:%S')
    timestamp = "Time: " + ts + " GMT"
    slider.text=timestamp

    FILENAME = BASE_FILENAME + str(state).zfill(4)
    SaveWindowAtts = SaveWindowAttributes()
    SaveWindowAtts.outputToCurrentDirectory = 1
    SaveWindowAtts.fileName = FILENAME
    SaveWindowAtts.family = 0
    #Set aspect ratio
    SaveWindowAtts.resConstraint = 0
    SaveWindowAtts.width = 1200 
    SaveWindowAtts.height = 800 
    SetSaveWindowAttributes(SaveWindowAtts)
    SaveWindow()

nframes = state + 1
command = 'ffmpeg -y -framerate 15 -f image2 -s 1200x800 -start_number 0 -i ' + BASE_FILENAME + '%04d.png -vframes ' + str(nframes) + '245 -vcodec libx264 -crf 25 -pix_fmt yuv420p ' + BASE_FILENAME + '.mp4'

exitcode = subprocess.call(command,shell=True)
if exitcode != 0:
    print('Error, exit code:',exitcode)
    print('Command:')
    print(command)
    sys.exit()

if do_rm == 'rm':
    subprocess.call('rm *.png',shell=True)

sys.exit()
