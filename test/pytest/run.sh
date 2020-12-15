docker container stop bglapi-test
docker container rm bglapi-test
docker build -t bglapi-test .
docker run --rm \
           --name bglapi-test \
           -v /home/ubuntu/bglapiserver/config:/config/ \
           -v /home/ubuntu/bglapiserver/test:/test \
           --net=host \
           -it bglapi-test -v -s