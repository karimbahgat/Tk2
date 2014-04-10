# Documentation for Tk2
Tk2 is a convenience library for extending the functionality of Tkinter, 
to make it easier and more flexible to create GUI applications. 

## Contents

### tk2.AddGradientBackground(...):
  Adds a gradient background to a widget.
  Note: The gradient works best on widgets whose width/height have been set manually as an option, and is not dynamically determined by a geometry manager.
  In particular, the gradient will not be updated to the new dimensions if your widget changes its size during runtime.
  If you are using a geometry manager to determine the size of the widget you can set the gradient width/height with the "auto" option.
  But be careful with doing this prior to the application has been created, since the actual sizes aren't fully negotiated until the application is fully created,
  and because to retrieve them this method has to update and thus display the window, which will look odd if it is still in its startup phase.
  
  - widget: the widget to give the gradient background. Note: The widget must support displaying images, so eg passing a root window or a Frame widget will result in an error.
  - colorstops: a list of RGB color tuples, each representing the colors to cycle through in the gradient. Must have at least two colors.
  - direction: a string indicating the direction of the gradient. "horizontal" to make it go to the right, or "vertical" to make it go upwards (default).
  - width: a string indicating how to determine the width of the gradient image. Set to "option" to read the width from the widget's width attribute (default) or "auto" to read the actual width as has been set by its geometry manager. Can also be specified directly as an integer.
  - height: a string indicating how to determine the height of the gradient image. Set to "option" to read the height from the widget's height attribute (default) or "auto" to read the actual height as has been set by its geometry manager. Can also be specified directly as an integer.

### tk2.AskColor(...):
  Pops up a temporary tk window asking user to visually choose a color.
  Returns the chosen color as a hex string. Also prints it as text in case
  the user wants to remember which color was picked and hardcode it in the script.
  
  - *text: an optional string to identify what purpose the color was chosen for when printing the result as text.

### tk2.Color(...):
  Returns a hex color string of the color options specified. Meant to allow
  greater flexibility and convenience than the builtin Tkinter color names.
  Is built on top of the Valentin Lab's Colour module which it uses behind
  the scenes. See: https://pypi.python.org/pypi/colour/0.0.5
  
  **Arguments:**
  
  | __option__    | __description__ | __input__
  | --- | --- | ---
  | basecolor | the human-like name of a color. Always required, but can also be set to 'random'. | string
  | *intensity | how strong the color should be. Must be a float between 0 and 1, or set to 'random' (by default uses the 'strong' style values, see 'style' below). | float between 0 and 1
  | *brightness | how light or dark the color should be. Must be a float between 0 and 1 , or set to 'random' (by default uses the 'strong' style values, see 'style' below). | float between 0 and 1
  | *style | a named style that overrides the brightness and intensity options (optional). |
  
  Valid style names are:
  
  - 'strong'
  - 'dark'
  - 'matte'
  - 'bright'
  - 'pastelle'

### tk2.Draggable(...):
  Makes a widget draggable
  MOSTLY WORKS, BUT CONTINUES TO DRAG EVEN AFTER RELEASETRIGGER IF SOME OTHER MOVEMENT IS STILL PROCESSING...
  Note: movepush, droppush, and effect are not currently working.
  
  - movepush: whether bumping into other widgets while being moved should push away the other widgets
  - droppush: whether releasing the drag over other widgets should push them away
  - effect: effect to use while dragging (eg MorphSize to bigger to give a lifting effect)
  - dragtrigger: tk trigger event string for when to start dragging, default is left mouseclick
  - releasetrigger: tk trigger event string for when to stop dragging, default is release of left mouseclick

### tk2.Jitter(...):
  Jitters/shakes the widget for a certain duration.
  
  - movepixels: maximum pixels to randomly shake from base position
  - frequency: how much time in comma seconds in between each shake movement
  - duration: how long in seconds the jitter should last
  - pindown: whether to center the jittering around the widget's original starting point or to let it jitter freely and end up in a new location

### tk2.MorphSize(...):
  Gradually changes the size of the widget
  WORK IN PROGRESS, INACCURATE CUS SIZE DEPENDENT ON TIME SPEED
  
  - sizechange: xtimes change in size (eg 2x twice as large), negative number of shrink, 1 if stay same, and 0 is not possible
  - duration: time in seconds it should take to morph to new size, currently not working properly

### tk2.MoveTo(...):
  Gradually moves a widget in a direct line towards endxy pixel coordinates.
  None of the options besides endxy are currently working.
  Note: requires that the widget uses a place manager (not pack or grid)
  
  - endxy: the end coordinate towards which to move the widget
  - speed: full speed pixels per ms
  - accel: 0 to 100 percentage speed buildup per ms
  - deaccel: 0 to 100 percentage speed lowering per ms
  - effect: some added effect to use on startup and slowdown (eg wobbly jello, shake)

### tk2.Partition(...) --> class object
  An instance representing a rectangular area of space, and is
  generated by the PartitionSpace function (not the user).
  Provides the user with easy access to that space's anchorpoints.
  The anchorpoints are given in the same format as what was used
  to create the partition in the first place, ie either absolute
  or relative xy coordinates.
  
  The anchorpoints are accessed as attributes and include:
  
  - .center: the xy center point of the partition
  - .width: the width of the partition
  - .height: the height of the partition
  - .nw: the northwest xy corner
  - .n: the north xy point
  - .ne: the northeast xy corner
  - .e: the east xy point
  - .se: the southeast xt corner
  - .s: the south xy point
  - .sw: the southwest xy corner
  - .w: the west xy point

  - #### .SubPartition(...):
    Creates additional subpartitions from this partition.
    Note: Can be buggy so only use if you really need to avoid nested widgets, eg if you need to structure your widgets over a large background image bc a background widget to nest them in would cover up parts of the image
    
    - partitions: how many subpartitions to create, integer
    - padx: how much padding to keep between each partition on the sides, integer for pixels or float for relative position.
    - pady: how much padding to keep between each partition on the top and bottom, integer for pixels or float for relative position.
    - direction: a string indicating in which direction to partition the space, "horizontal" (default) or "vertical".

### tk2.PartitionSpace(...):
  Partitions an abstract coordinate space into subdivisions,
  returning multiple Partition instances which provide easy
  access to the various anchorpoints of each partition.
  Useful for placing widgets at regular spaced out intervals
  when using the Tkinter .place geometry manager, which
  usually requires the user to set positions manually.
  The original coordinate space can be defined as pixels or
  relative positions.
  
  - xtox: a two-item list or tuple containing the leftmost and rightmost x position, in that order. For each use integer for pixels or float for relative position.
  - ytoy: a two-item list or tuple containing the topmost and bottommost y position, in that order. For each use integer for pixels or float for relative position.
  - partitions: how many subpartitions to create, integer
  - padx: how much padding to keep between each partition on the sides, integer for pixels or float for relative position.
  - pady: how much padding to keep between each partition on the top and bottom, integer for pixels or float for relative position.
  - direction: a string indicating in which direction to partition the space, "horizontal" (default) or "vertical".
  
  Example:
  
  ```
  import Tkinter as tk
  import tk2
  
  win = tk.Tk()
  frame = tk.Frame(win, width=500, height=500)
  frame.pack()
  
  for partition in tk2.PartitionSpace(xtox=(200,500), ytoy=(200,500), partitions=5, padx=10, pady=10):    
      #first get partition info
      partx,party = partition.center
      partwidth,partheight = partition.width,partition.height
      
      #then place widget using partition info
      widget = tk.Label(frame, bg="blue")
      widget.place(x=partx, y=party, width=round(partwidth), height=round(partheight), anchor="center")
  ```

### tk2.SetEnterAnim(...):
  Gives a widget an enter animation. Once this has been set, the widget will be hidden at startup, and will only enter if its enter trigger event occurs.
  
  - anim: the type of entrance animation. For now only "fly in" works. Going to add later: peek up, fade in??, flicker in, shrink/grow in, etc.
  - trigger: the GUI event that will trigger the entrance animation, given as a string the same way triggers are assigned to Tkinter trace events, eg '<Button-1>'. 

