#Review of my first shell scripting program.
ari.py

My first shell scripting program is about to calculate Automated redability index of text files.
The automated readability index is a readability test designed to measure the how easy our text is to understand.
Its calculated by using the Formula :4.71 x (characters/words) + 0.5 x (words/sentences) – 21.43.

The grade level will be different according to the ARI value :
That means:
Score Age 	Grade Level
1 	  5-6 	Kindergarten
2 	  6-7 	First Grade
3 	  7-8 	Second Grade
4 	  8-9 	Third Grade
5 	  9-10 	Fourth Grade
6 	 10-11 	Fifth Grade
7 	 11-12 	Sixth Grade
8 	 12-13 	Seventh Grade
9 	 13-14 	Eighth Grade
10 	 14-15 	Ninth Grade
11 	 15-16 	Tenth Grade
12 	 16-17 	Eleventh Grade
13 	 17-18 	Twelfth Grade
14 	 18-22 	College student 

The basic idea about to solve the problem is :
1.Read the file content.
2.Find the number of characters,words and sentance present in the file.
3.Declar a function(calculate_ari) pass these value as argument.By using these value calculate ARI.
4.The ARI passsed to an another function(determine_grade_level) for finding grade.

How I find solution :
#Read file content



