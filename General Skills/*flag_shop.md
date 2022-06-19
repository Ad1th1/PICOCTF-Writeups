This is an awesome CTF to help one get acquainted with buffer overflows.

I knew that I would have to get a large enough negative number at first to get my balance higher. A quick look at the code told me that it was useless to supply a large negative number, as there is a check on the positivity of the number supplied, lol.

So I was clueless on how to proceed and watched this amazing video = https://www.youtube.com/watch?v=F5J6MG0mD-A

I realized that I needed a value greater than the int32 limit to get a negative number.

The int32 limit is 2,147,483,647

Since the number of flags * 900 needs to be greater than the above limit for an overflow, I did some cute lil division to get the required number.

I plugged this in and got a negative amount subtracted from my account. Hallelujah!!!
After this, I bought the required flag and grinned at the sight of the flag...


Note to self: You got this! Chill and jeep going. One day, the whole picture will be visible. For now, keep putting the pieces together...
