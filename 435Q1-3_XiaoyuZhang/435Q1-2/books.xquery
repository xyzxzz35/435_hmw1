for $book in doc("books.xml")/catalog/book
order by xs:float($book/price) ascending
return $book/title


doc("books.xml")//book[author = 'Rajati']

for $a in distinct-values(doc("books.xml")//author)
return <res>
 <name>{$a}</name>
 <count>
 {count(doc("books.xml")//book[exists(index-of(author,$a))]) }
 </count>
 </res>
