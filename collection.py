# Muhammad Haroon Nasir
# August 6th, 2025

# creates dictionary and then prints a sentence formed with the key and value of each instance


# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
    }

for author, date in authors.items():
    print("%s died in %d." % (author, int(date)))

