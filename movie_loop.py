#Calendar
import datetime
import calendar

#Choose dataset and timestamp modifier
db = "outputs_shiny-le/output_nosinkout/leem_0001.nc"
t_start = calendar.timegm(datetime.datetime(1858, 11, 17, 0, 0, 0).timetuple())
#db = "outputs_shiny-le/output_sinkout/leem_0001.nc"
#t_start = calendar.timegm(datetime.datetime(1858, 11, 17, 0, 0, 0).timetuple())
#db = "outputs_shiny-le/output_leem/TP_crop.nc"
#t_start = calendar.timegm(datetime.datetime(2013, 3, 1, 0, 0, 0).timetuple())


#Restore a session file
#RestoreSessionWithDifferentSources("tp_layer1.session", 0, db)
#RestoreSessionWithDifferentSources("tp_layer19.session", 0, db)
RestoreSessionWithDifferentSources("tp_3D_slice.session", 0, db)
#RestoreSessionWithDifferentSources("tp_3D.session", 0, db)

#Name the file
BASE_FILENAME = "TP_nosinkout_layer1_"

#Create a time slider
slider = CreateAnnotationObject("TimeSlider")
slider.text = ""
slider.height = 0.05
slider.width = 0.3
slider.position = (0.03, 0.94)
m = GetMetaData(db)

for state in range(TimeSliderGetNStates()): 
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
    SaveWindowAtts.width = 800 
    SaveWindowAtts.height = 480 
    SetSaveWindowAttributes(SaveWindowAtts)
    SaveWindow()

sys.exit()
