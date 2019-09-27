# CAMO
CAMO - A Context-aware Movie Ontology, presents a movie ontology which was build up using contextual features extracted from Linked Open Data (LOD) and movie databases (Rotten Tomatoes and IMDB). The current version of CAMO contains only user context and item context representing data. Item context can be further categorized as representational context and interactional context. The representational context of a movie includes cast and crew, rating, certification, and genre that are retrieved from Rotten Tomatoes, IMDB and LOD.
On the other hand, interactional context represents the opinion components that expressed by the movie viewers in their reviews
.

# DOCUMENTATION
## CLASSES
In CAMO, we have used eight different classes (concepts)  
1. Class: http://www.semanticweb.org/administrator/ontologies/2017/2/CAMO_Ontology-Schema#Genre  
This class contains 20 genres used in movies such as, Action and Adventure, Art House and International, Comedy, Crime, Animation,
Documentary, Sports, Drama, and Faith and Spirituality.  
2. Class: http://www.semanticweb.org/administrator/ontologies/2017/2/CAMO_Ontology-Schema#SubGenre  
This is a sub-class of each of the genre class. Individuals or instances of sub-genre class further extended the genre.  
3. Class: http://www.semanticweb.org/administrator/ontologies/2017/2/CAMO_Ontology-Schema#Certification  
With every movie, a certificate attached which gives the information about violence and gore, profanity, alchol, drugs and smoking, frightening and intense scenes and sex and nudity. Each country has categorized there certification with different labeling.  
4. Class: http://www.semanticweb.org/administrator/ontologies/2017/2/CAMO_Ontology-Schema#Awards  
Awards class contains three instances Golden Globe, Academy (Oscar), and BAFTA award. Movies which have won these awards in any categories are assigned to the individuals of this class.  
5. Class : http://www.semanticweb.org/administrator/ontologies/2017/2/CAMO_Ontology-Schema#CastandCrew  
This class have the actor (contains the name of all the actors belongs to the collected movies), actress (contains the name of all the actress belongs to the collected movies), and Director (contains the name of all the directors belongs to the collected movies) instances.  
6. Class : http://www.semanticweb.org/administrator/ontologies/2017/2/CAMO_Ontology-Schema#Movie  
This is the root class of the ontology which is connected to all the sub-classes present in the CAMO mentioned above. This class contains basic movie information which includes title, abstract, rating, based-on, and releasing dates.  
7. For each movie, we have calculated the sentiment score from the viewers review. NLP classifier(an IBM Watson API) is used to identify various interactional context, such as cast performance, cinematography, etc. from review documents. CAMO contains contextual information about 1104 movies retrieved from Rotten Tomatoes, IMDB, DBpedia, and review documents generated by 174756 users and 5650 critics.  
   a). Story  
      Class : http://www.semanticweb.org/administrator/ontologies/2017/2/CAMO_Ontology-Schema#storySentimentValue  
   b). Cinematography  
      Class : http://www.semanticweb.org/administrator/ontologies/2017/2/CAMO_Ontology-Schema#cinematographySentimentValue  
   c). Music  
      Class : http://www.semanticweb.org/administrator/ontologies/2017/2/CAMO_Ontology-Schema#musicSentimentValue  
   d). Visual Effects  
      Class : http://www.semanticweb.org/administrator/ontologies/2017/2/CAMO_Ontology-Schema#visualEffectsSentimentValue  
   e). Cast Acting  
      Class : http://www.semanticweb.org/administrator/ontologies/2017/2/CAMO_Ontology-Schema#castPerformancesSentimentValue  
   f). Scenes  
      Class : http://www.semanticweb.org/administrator/ontologies/2017/2/CAMO_Ontology-Schema#scenesSentimentValue  
   g). Direction  
      Class : http://www.semanticweb.org/administrator/ontologies/2017/2/CAMO_Ontology-Schema#directionSentimentValue  
   h). Awards  
      Class : http://www.semanticweb.org/administrator/ontologies/2017/2/CAMO_Ontology-Schema#awardsSentimentValue  
8. The last class is based-on the reviewers who write reviews in movies.  

## OBJECT PROPERTIES  
In CAMO we have used object properties to connect the individuals of different classes. These object properties are predicates that connects subjects and objects. A few object properties used in CAMO are hasCertification, hasSubGenre, hasStorySentiments, and directedBy.



# DOWNLOADS

To run CAMO on your system, first, you need to download the CAMO owl file. Once the owl file is downloaded, this file can be run by using either Protege(https://protege.stanford.edu/) or Apache Jena Fuseki (https://jena.apache.org/)/ server.


