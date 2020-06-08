from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpRequest, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Prefetch
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.db.models import F
from django.db.models import Avg
from .models import *
from sklearn.metrics import jaccard_similarity_score
from django.core.management.base import BaseCommand, CommandError



def jaccardsimilarity(request):

	feature_dict={}	
	movie_list=[]

	for kk in range(1,1103):
		movie_list.append(kk)

	
	new_list=[]

	for moviename in movie_list:

		for i in Movie_Details.objects.filter(id=moviename):
			m1_string = i.genre
			m1_genre = m1_string.split(',')

			y1_string = i.sub_genre
			m1_sub_genre = y1_string.split(',')

			d1_string = i.director.encode('utf-8')
			m1_director = d1_string.split(',')

			ca1_string = i.cast.encode('utf-8')
			m1_cast = ca1_string.split(',')


			based_on1_string = i.based_on
			m1_based_on = based_on1_string.split(',')

			about1_string = i.about
			m1_about = about1_string.split(',')

			movie_topics_lda_string1 = str(i.movie_topics_lda)
			movie_topics_lda1 = movie_topics_lda_string1.split(', ')		

			rating1 = i.rating[:3]

			theatre1 = i.theatre_release[:4]



			for k in Movie_Details.objects.all():
				aUb=0
				aIb=0
				total_features=[]
				m2_string = k.genre
				m2_genre = m2_string.split(',')

				y2_string = k.sub_genre
				m2_sub_genre = y2_string.split(',')

				d2_string = k.director.encode('utf-8')
				m2_director = d2_string.split(',')

				ca2_string = k.cast.encode('utf-8')
				m2_cast = ca2_string.split(',')

				based_on2_string = k.based_on
				m2_based_on = based_on2_string.split(',')

				about2_string = k.about
				m2_about = 	about2_string.split(',')

				movie_topics_lda_string2 = str(k.movie_topics_lda)
				movie_topics_lda2 = movie_topics_lda_string2.split(', ')	
				
				rating2 = k.rating[:3]

				theatre2 = k.theatre_release[:4]
				
				genre1 = Counter(m1_genre)
				genre2 = Counter(m2_genre)

				sub_genre1=Counter(m1_sub_genre)
				sub_genre2=Counter(m2_sub_genre)

				director1 = Counter(m1_director)
				director2 = Counter(m2_director)

				
				cast1 = Counter(m1_cast)
				cast2 = Counter(m2_cast)

				based_on1 = Counter(m1_based_on)
				based_on2 = Counter(m2_based_on)

				about1 = Counter(m1_about)
				about2 = Counter(m2_about)

				movie_topic1=Counter(movie_topics_lda1)
				movie_topic2=Counter(movie_topics_lda2)
				

				b3 = [val for val in genre1 if val in genre2]
				b4 = [val for val in sub_genre1 if val in sub_genre2]
				b5 = [val for val in director1 if val in director2]
				b6 = [val for val in cast1 if val in cast2]
				b7 = [val for val in based_on1 if val in based_on2]
				b8 = [val for val in about1 if val in about2]
				b10 = [val for val in movie_topic1 if val in movie_topic2]
				
				
				rating_sum = (10 - abs(float(rating1)-float(rating2)))/10
				aIb = len(b3) + len(b4) + len(b5) + len(b7) + len(b8) + len(b10) +rating_sum

				total_features.extend([m1_genre,m2_genre,m1_sub_genre,m2_sub_genre,m1_director,m2_director,m1_based_on,m2_based_on,m1_about,m2_about,movie_topics_lda1,movie_topics_lda2])
				flat_list = [item for sublist in total_features for item in sublist]
					
				

	
				aUb = len(list(set(flat_list)))	
					
				jacard_similarity = float(aIb*1.0/aUb)
					
				
				feature_dict[k.name.encode('utf-8')] = jacard_similarity
				
				
				
		

			import operator
			
			sorted_x = sorted(feature_dict.items(), key=operator.itemgetter(1))
			
			
			for m in Movie_Details.objects.filter(id=moviename):

			

				m.movie_similarity_jaccard = sorted_x

				m.save()

				print m.id

				print m.name.encode('utf-8')

## Rating Prediction using Jaccard Similarity

def jaccardsimilarityprediction(request):

	query_list = []
	mae=[]
	movie_list_mae = [10] ##Type the movie id for which ratings need to predict
	s=Reviewer_Profile.objects.raw('SELECT id,reviewer_name,reviewer_id, count(reviewer_id) FROM moviedb2.app_imdb_reviewer_profile group by reviewer_id having count(reviewer_id) between 30 and 50;')

	for k in s:

		query_list.append(k.reviewer_id)

	print query_list

	for mov in movie_list_mae:


	
		for q in query_list:

			

			for rw in Reviewer_Profile.objects.filter(reviewer_id__icontains=q):

				if rw.movie_ratings:

					if rw.movie_name_id == mov:		

						

			
						list12=[]
						simt_dict={}
						user_movie=[]
						user_movie1=[]
						n22={}
						movie_id={}
						import ast
						import operator
						import itertools
						from itertools import islice
						for i in Movie_Details.objects.filter(id=mov):

							new_dict=(i.movie_similarity_jaccard)
							
						simt_dict = dict(list(ast.literal_eval(new_dict)))

						sorted_x = sorted(simt_dict.items(), key=operator.itemgetter(1))

						sorted_dict = dict(sorted_x[-30:]) ## Top-k similar movies
						print sorted_dict
						#import pdb;pdb.set_trace()
						

						

						
						for i in Reviewer_Profile.objects.filter(reviewer_id__icontains=q):
							user_movie.append(i.movie_name_id)

						print user_movie	
						for k in Movie_Details.objects.all():
							for i in user_movie:
								if k.id==i:
									user_movie1.append(k.name)
						#print user_movie1			
						
						
						n22 = {k: sorted_dict[k] for k in sorted_dict.viewkeys() & set(user_movie1)}

						print n22

						for b in Movie_Details.objects.all():

							movie_id[b.name] = b.id

						#print movie_id

						flat_lis = dict((movie_id[key], value) for (key, value) in n22.items())

						for r in flat_lis:

							for s in Movie_Details.objects.filter(id=r):

								print s.name
								print ('\n')
						
						mu = 6.12
						user_rating_count = 0
						no_of_movie = 0
						for k in Reviewer_Profile.objects.filter(reviewer_id__icontains=q):

							if k.movie_ratings:
								no_of_movie = no_of_movie +1
								user_rating_count = user_rating_count + int(k.movie_ratings[:1])

						bu = float(user_rating_count)/no_of_movie
								
						if (mu>bu):
							bu = mu - bu
							bu=bu*(-1)
						if (mu<bu):
							bu=bu-mu	

						movie_rat = 0
						count_movie = 0	
						for r in Movie_Details.objects.filter(id=mov):
							
							#if r.movie_ratings:
								#count_movie = count_movie +1
								#movie_rat = movie_rat + int(r.movie_ratings[:1])
							
							bi = float(r.rating[:3])	
						#bi = float(movie_rat)/count_movie
						
						if (mu>bi):
							bi = mu - bi
							bi=bi*(-1)
						if (mu<bi):
							bi=bi-mu		

						


						total_similarity=0
						count_loop = 0
						sim_value = 0
						if flat_lis:
							for key, value in flat_lis.iteritems():
							
							
								for k in Reviewer_Profile.objects.filter(reviewer_id__icontains=q):

									if k.movie_ratings:

										if (key == k.movie_name_id):

											count_loop=count_loop+1



											sim_value = sim_value + (value)

											total_similarity = total_similarity + (float(k.movie_ratings[:1]) * float (value))
						else:
							count_loop = 1

						if sim_value==0:	
							similarity_score = float(total_similarity)/1
						else:
							similarity_score = float(total_similarity)/sim_value	

						print rw.reviewer_name

						f=open('mean_absolute_error_new_list.txt','a')

						f.write(rw.reviewer_name)

						f.write('\t')

						f.write(rw.movie_ratings)

						f.write('\t')

						differ = float(int(rw.movie_ratings[:-3]) - ( similarity_score))

						f.write(str(differ))

						print differ

						f.write('\n')

						f.close()				