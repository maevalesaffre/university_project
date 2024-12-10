FROM ubuntu:20.04

# Install gcc and makefile to compile the tests
RUN apt-get update && \
    apt-get install -y gcc make && \
    apt-get clean

# Create a user and a directory to work with
RUN groupadd -g 999 runner && \
    useradd -r -u 999 -g runner runner
WORKDIR /eval
RUN chown runner:runner /eval
USER runner

# Copy files that shouldn't change before
COPY --chown=runner:runner test_cases/run_tests.sh Makefile /eval/
COPY --chown=runner:runner test_cases /eval/test_cases

# Copy the file containing the answers
COPY --chown=runner:runner *.c *.h /eval/

# We are ready to compile & test
ENTRYPOINT ["make"]