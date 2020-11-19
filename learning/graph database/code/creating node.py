from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "wentihenda"))


def create_friend_of(tx, name, friend):
    tx.run("CREATE (a:Person)-[:KNOWS]->(f:Person {name: $friend})"
           "WHERE a.name = $name "
           "RETURN f.name AS friend", name=name, friend=friend)


with driver.session() as session:
    session.write_transaction(create_friend_of, "Alice", "Bob")


with driver.session() as session:
    session.write_transaction(create_friend_of, "Alice", "Carl")

driver.close()


def get_friends_of(tx, name):
    friends = []
    result = tx.run("MATCH (a:Person)-[:KNOWS]->(f) "
                         "WHERE a.name = $name "
                         "RETURN f.name AS friend", name=name)
    for record in result:
        friends.append(record["friend"])
    return friends

with driver.session() as session:
    friends = session.read_transaction(get_friends_of, "Alice")
    for friend in friends:
        print(friend)

driver.close()