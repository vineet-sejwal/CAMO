# CAMO
CAMO - A Context-aware Movie Ontology, presents a movie ontology which was build up using contextual features extracted from Linked Open Data (LOD) and movie databases (Rotten Tomatoes and IMDB). The current version of CAMO contains only user context and item context representing data. Item context can be further categorized as representational context and interactional context. The representational context of a movie includes cast and crew, rating, certification, and genre that are retrieved from Rotten Tomatoes, IMDB and LOD.
On the other hand, interactional context represents the opinion components that expressed by the movie viewers in their reviews
.

# DOCUMENTATION
In CAMO, we have used eight different classes (concepts)  
Class: http://www.semanticweb.org/administrator/ontologies/2017/2/CAMO_Ontology-Schema#Genre  
This class contains 20 genres used in movies such as, Action and Adventure, Art House and International, Comedy, Crime, Animation,
Documentary, Sports, Drama, and Faith and Spirituality.  
Class: http://www.semanticweb.org/administrator/ontologies/2017/2/CAMO_Ontology-Schema#SubGenre  
This is a sub-class of each of the genre class. Individuals or instances of sub-genre class further extended the genre.  
Class: http://www.semanticweb.org/administrator/ontologies/2017/2/CAMO_Ontology-Schema#Certification  
With every movie, a certificate attached which gives the information about violence and gore, profanity, alchol, drugs and smoking, frightening and intense scenes and sex and nudity. Each country has categorized there certification with different labeling.  
Class: http://www.semanticweb.org/administrator/ontologies/2017/2/CAMO_Ontology-Schema#Awards  
Awards class contains three instances Golden Globe, Academy (Oscar), and BAFTA award. Movies which have won these awards in any categories are assigned to the individuals of this class.  
Class : http://www.semanticweb.org/administrator/ontologies/2017/2/CAMO_Ontology-Schema#CastandCrew  
This class 



# DOWNLOADS

To run CAMO on your system, first, you need to download the CAMO owl file. Once the owl file is downloaded, this file can be run by using either Protege(https://protege.stanford.edu/) or Apache Jena Fuseki (https://jena.apache.org/)/ server.


