## SCRIPTS

Random snippets (that aren't important enough to warrant their own repository, but not trivial enough to delete either) that make the world a better place

###### EDL PARSER

An edit decision list or EDL is used in the post-production process of film editing and video editing. The list contains an ordered list of reel and timecode data representing where each video clip can be obtained in order to conform the final cut. [Wikipedia](https://en.wikipedia.org/wiki/Edit_decision_list)

Video editors (the people) currently need to manually write down the the music they use in their videos into an Excel file (in order to pay licensing fees). That's dumb. However, Adobe Premiere allows the user to extract the .edl files that feature all the necessary information (artist, song, label, duration).

This script parses .edl files into .xlsx files, as best as it can. It extracts the artist, song, label, duration, dumps other unnecessary data and nicely writes them into an Excel file.