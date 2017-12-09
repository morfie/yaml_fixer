docker build -t=yamlfilter .
docker run -i --rm yamlfilter pygmentize -O encoding=utf-8 -f text -l yaml -F servicefilter < FILE