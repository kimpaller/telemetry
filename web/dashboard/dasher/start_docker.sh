set -e

helpFunction()
{
   echo ""
   echo "Usage: $0 [option]"
   echo --stop "\t exits after stoping and removing container"
   exit 1 # Exit script after printing help
}

while [ -n "$1" ]
do
case "$1" in
--stop) echo "stopping and removing container only" && STOP=true;;
*) echo "$1 is not an option" && helpFunction;;
esac
shift
done

# Stop and remove existing container
IMAGE=$(docker ps -q --filter ancestor="constellation" )
if [ "$IMAGE" ]
then
	echo "FOUND"
	docker stop $IMAGE
	docker rm $IMAGE
fi

# if --stop is set, do not proceed creating new container
if [ ! -z ${STOP+x} ]; then return 0; fi

[ -d "telemetry_src" ] && rm -rf "telemetry_src"
OLD_PATH=`pwd`
cd ../../../../.
cp -r telemetry telemetry_src
mv telemetry_src telemetry/web/dashboard/dasher/
cd $OLD_PATH

docker build -t constellation .
docker run -d --restart unless-stopped -p 5000:5000 constellation
