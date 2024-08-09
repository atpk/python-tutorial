import pysolr
import json

# Connect to Solr
solr_url = 'http://localhost:8983/solr/hybrid_search'
solr = pysolr.Solr(solr_url, always_commit=True, timeout=10)

# Additional data to be indexed
additional_data = [
    {
        "id": "3",
        "source": "Gullivers_Travels_Novel_.pdf",
        "page": 16,
        "content": "Page 17 of 137 \nCHAPTER V  \n[The author, by an extraordinary strata gem, prevents an invasion. A high title of honour is \nconferred upon him. Ambassadors arrive from the emperor of Blefuscu, and sue for peace. \nThe empress's apartment on fire by an accident; the author instrumental in saving the rest of \nthe palace .] \nThe em pire of Blefuscu is an island situated to the north -east of Lilliput, from which it is \nparted only by a channel of eight hundred yards wide. I had not yet seen it, and upon this \nnotice of an intended invasion, I avoided appearing on that side of the coast,  for fear of being \ndiscovered, by some of the enemy's ships, who had received no intelligence of me; all \nintercourse between the two empires having been strictly forbidden during the war, upon pain \nof death, and an embargo laid by our emperor upon all vess els whatsoever. I communicated \nto his majesty a project I had formed of seizing the enemy's whole fleet; which, as our scouts"
    },
    {
        "source": "Gullivers_Travels_Novel_.pdf",
        "id": "4",
        "page": 19,
        "content": "presence of her chief confidents could not forbear vow ing revenge.  \nCHAPTER VI  \n[Of the inhabitants of Lilliput; their learning, laws, and customs; the manner of educating \ntheir children. The author's way of living in that country. His vindication of a great lady. ] \nAlthough I intend to leave the description of this empire to a particular treatise, yet, in the \nmean time, I am content to gratify the curious reader with some general ideas. As the \ncommon size of the natives is somewhat under six inches high, so there is an exact proportion \nin all othe r animals, as well as plants and trees: for instance, the tallest horses and oxen are \nbetween four and five inches in height, the sheep an inch and half, more or less: their geese \nabout the bigness of a sparrow, and so the several gradations downwards till  you come to the \nsmallest, which to my sight, were almost invisible; but nature has adapted the eyes of the"
    },
    {
        "id": "5",
        "source": "Gullivers_Travels_Novel_.pdf",
        "page": 9,
        "content": "be lost or spoiled if I ventured them out of my possession.  \nCHAPTER III  \n[The author diverts the emperor, and his nobility of both sexes, i n a very uncommon manner. \nThe diversions of the court of Lilliput described. The author has his liberty granted him upon \ncertain conditions. ] \nMy gentleness and good behaviour had gained so far on the emperor and his court, and \nindeed upon the army and pe ople in general, that I began to conceive hopes of getting my \nliberty in a short time. I took all possible methods to cultivate this favourable disposition. The \nnatives came, by degrees, to be less apprehensive of any danger from me. I would sometimes \nlie down, and let five or six of them dance on my hand; and at last the boys and girls would \nventure to come and play at hide -and-seek in my hair. I had now made a good progress in \nunderstanding and speaking the language. The emperor had a mind one day to ente rtain me"
    },
    {
        "id": "6",
        "source": "Gullivers_Travels_Novel_.pdf",
        "page": 2,
        "content": "Page 3 of 137 \n prudent method to lie still, and my design was to continue so till night, when, my  left hand \nbeing already loose, I could easily free myself: and as for the inhabitants, I had reason to \nbelieve I might be a match for the greatest army they could bring against me, if they were all \nof the same size with him that I saw. But fortune dispose d otherwise of me. When the people \nobserved I was quiet, they discharged no more arrows; but, by the noise I heard, I knew their \nnumbers increased; and about four yards from me, over against my right ear, I heard a \nknocking for above an hour, like that of people at work; when turning my head that way, as \nwell as the pegs and strings would permit me, I saw a stage erected about a foot and a half \nfrom the ground, capable of holding four of the inhabitants, with two or three ladders to \nmount it: from whence on e of them, who seemed to be a person of quality, made me a long"
    }
]

# Convert additional data to the same format as the example data
for doc in additional_data:
    doc["title"] = f"{doc['source']} - Page {doc['page']}"

# Add documents to Solr
solr.add(additional_data)

print("Data indexed successfully.")