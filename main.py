import wx
import wx.xrc
import wx.dataview
import matplotlib.pyplot as plt
import numpy as np

from VerticalSquare import MainWindowAbstract


class MainWindow (MainWindowAbstract):
    def __init__(self, parent):
        super().__init__(parent)
        self.m_FilePicker.SetInitialDirectory(".")

    def onExit( self, event ):
        self.Destroy()

    def onCreatePlot( self, event ):
        selectedFilepath = self.m_FilePicker.GetPath()
        print(selectedFilepath)
        self.AlterFileToProperFormat(selectedFilepath)
        
    def AlterFileToProperFormat(self, incomingFile):
        selectedFile = incomingFile
        
        with open(selectedFile, 'r') as file:
            data = file.readlines()
            

        #^ Delete any elements that don't match REGEX for VTS data
            self.readingsOnly = []
            for i in range(len(data)):
                if len(data[i]) == 8:
                    self.readingsOnly.append(data[i])
           
        #^ Add a comma after the 4th character in each line
        commaAdded = "\n".join("".join(line[i : i + 4] for i in range(0, len(line), 4)) for line in self.readingsOnly)
        commaAdded = commaAdded.split()

        while("" in commaAdded):
            commaAdded.remove("")
          
        #^ Get only data values (not the incorrect x axis)
        justData = [x[:-3] for x in commaAdded]
        
        #^ Remove any null "0000" values
        noNulls = [x for x in justData if x !='0000']
        
        
        #^ Convert from Hex to Decimal
        decimalVals = []
        for i in range(len(noNulls)):
            val = int(noNulls[i], 16)
            decimalVals.append(val)
            
        dataPoints = len(decimalVals)
        
       
        self.UpdateMinMaxGUI(decimalVals)                     
        self.WriteToFile(decimalVals)
        self.ChartData(decimalVals, dataPoints)
        
        
    def UpdateMinMaxGUI(self, incomingList):
        allVals = incomingList
        minVal = min(allVals)
        maxVal = max(allVals)
        delta = maxVal-minVal
        
        self.m_MAX_VAL.SetLabelText(str(maxVal))
        self.m_MIN_VAL.SetLabelText(str(minVal))
        self.m_DELTA_VAL.SetLabelText(str(delta))
        
        if delta > 105:
            self.m_DELTA_VAL.SetBackgroundColour("Red")
        else:
            self.m_DELTA_VAL.SetBackgroundColour("Green")
        
        
    def WriteToFile(self,incomingList):
        values = incomingList
        with open("./Vertical-Formatted.log",'w') as newFile:
            for line in values:
                newFile.write(str(line) + '\n')

    def ChartData(self, incomingList, incmoningLength):
        toChart = incomingList
        numPoints = incmoningLength
        x = np.linspace(int(1),int(numPoints),int(numPoints)) #(x_start, x_end, the total number of y points that will be plotted) 
        y = toChart

        plt.xlabel("X Axis")
        plt.ylabel("Thickness Profile")
        plt.title("Vertical Profile")
        plt.tight_layout()
        
        plt.plot(x, y, label="Vertical Profile", color='red')
        
        windowTitle = "Side Vertical Profile"
        fig = plt.gcf()
        fig.canvas.manager.set_window_title(windowTitle)
        
        plt.show()
        



app = wx.App()
frame = MainWindow(None)
frame.SetMaxSize(wx.Size(300,250))
frame.SetMinSize(wx.Size(300,250))
frame.Show()
app.MainLoop()