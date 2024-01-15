FROM python:3.9-slim
WORKDIR /asset-image
COPY ./ /asset-image/
CMD [ "python","main.py" ]
#terminal
#docker image build -t asset-app:1.0 ./
#docker tag asset-app:1.0 saqib4321/asset-app:1.0