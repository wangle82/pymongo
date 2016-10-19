from elasticsearch import Elasticsearch

test="10.15.226.153"
online = "10.15.212.31";
es = Elasticsearch(hosts=online)

search = es.search(index='chapter',q='bookId:100069855')

print(search)