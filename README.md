### Convex coding exercise

# Running the code
    docker-compose build
    docker-compose run --rm convex-evaluation


# Initial Instructions
Attached, find the file `events.csv`, which contains a log of events with an
associated customer\_id and timestamp.

Your task is to write a program that answers the following question:

- How many events did customer X send in the one hour buckets between timestamps A and B?

Choice of language, platform, and libraries is left up to you. Please include instructions for how to run your program.

The team uses all recent versions of macOS with current Docker.

We expect this exercise to take 1-3 hours.

**Bonus:** 
- Include an HTTP service that answers the same question.


# Considerations
- All in memory. Only 15M, so it's not bad to read the whole thing in.
- One hour buckets? Is that referencing the data? Is each line a 1 hour bucket, or do I round to the nearest hour
