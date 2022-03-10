# fonto-backend

Running backend.py will output an output.csv file which will contain the data in the desired format.
I had a helper function which converted australian_post_codes.txt to a json file so I can open it at runtime for faster search.

In regards to design considerations, I also made a road_types dictionary to reduce search time when looping through the string to look for the word that would identify the road.

I found it most difficult thinking of an efficient way to identify the road in the input string. 

Admittedly, the one restriction is that I won't be able to correctly parse a road whose name is a road type. 
