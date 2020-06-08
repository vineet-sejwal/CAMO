
def PICSS_CAMO(request):

	import math
	
	feature_dict={}	
	movie_list =[]

	import itertools as it
	
	movie_list = [] ## Write the movie id

	for moviename in movie_list:
		a_list_genre = []

		a_list_sub_genre =[]

		a_list_director =[]

		a_list_based_on=[]

		a_list_about =[]

		a_list_movie_topics =[]

		for i in Movie_Details.objects.filter(id=moviename):
			print i.name
			m1_string = i.genre
			m1_genre = m1_string.split(',')
			a_list_genre.append(m1_genre)

			y1_string = i.sub_genre
			m1_sub_genre = y1_string.split(',')
			a_list_sub_genre.append(m1_sub_genre)

			d1_string = i.director.encode('utf-8')
			m1_director = d1_string.split(',')
			a_list_director.append(m1_director)

			ca1_string = i.cast.encode('utf-8')
			m1_cast = ca1_string.split(',')


			based_on1_string = i.based_on
			m1_based_on = based_on1_string.split(',')
			a_list_based_on.append(m1_based_on)

			about1_string = i.about
			m1_about = about1_string.split(',')
			a_list_about.append(m1_about)

			movie_topics_lda_string1 = str(i.movie_topics_lda)
			movie_topics_lda1 = movie_topics_lda_string1.split(', ')	
			a_list_movie_topics.append(movie_topics_lda1)


			rating1 = i.rating[:3]

			theatre1 = i.theatre_release[:4]
			list222=[]
			

			for k in Movie_Details.objects.all():

				b_list_genre = []

				b_list_sub_genre =[]

				b_list_director =[]

				b_list_based_on=[]

				b_list_about =[]

				b_list_movie_topics =[]

				m2_string = k.genre
				m2_genre = m2_string.split(',')
				b_list_genre.append(m2_genre)

				y2_string = k.sub_genre
				m2_sub_genre = y2_string.split(',')
				b_list_sub_genre.append(m2_sub_genre)

				d2_string = k.director.encode('utf-8')
				m2_director = d2_string.split(',')
				b_list_director.append(m2_director)

				ca2_string = k.cast.encode('utf-8')
				m2_cast = ca2_string.split(',')

				based_on2_string = k.based_on
				m2_based_on = based_on2_string.split(',')
				b_list_based_on.append(m2_based_on)

				about2_string = k.about
				m2_about = 	about2_string.split(',')
				b_list_about.append(m2_about)

				movie_topics_lda_string2 = str(k.movie_topics_lda)
				movie_topics_lda2 = movie_topics_lda_string2.split(', ')	
				b_list_movie_topics.append(movie_topics_lda2)
				
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
				
				b9 = len(b3) + len(b4) + len(b5) + len(b7) + len(b8) 
				#import pdb;pdb.set_trace()
				rating_sum = (10 - abs(float(rating1)-float(rating2)))/10
				#import pdb;pdb.set_trace()
				a_set_genre = set([item for sublist in a_list_genre for item in sublist])

				a_set_sub_genre = set([item for sublist in a_list_sub_genre for item in sublist])

				a_set_director = set([item for sublist in a_list_director for item in sublist])

				a_set_based_on = set([item for sublist in a_list_based_on for item in sublist])

				a_set_about = set([item for sublist in a_list_about for item in sublist])

				a_set_movie_topics = set([item for sublist in a_list_movie_topics for item in sublist])

				b_set_genre = set([item for sublist in b_list_genre for item in sublist])

				b_set_sub_genre = set([item for sublist in b_list_sub_genre for item in sublist])

				b_set_director = set([item for sublist in b_list_director for item in sublist])

				b_set_based_on = set([item for sublist in b_list_based_on for item in sublist])

				b_set_about = set([item for sublist in b_list_about for item in sublist])

				b_set_movie_topics = set([item for sublist in b_list_movie_topics for item in sublist])

				# Finding the set difference a-b

				set_difference_genre = list(a_set_genre - b_set_genre)

				set_difference_sub_genre = list(a_set_sub_genre - b_set_sub_genre)

				set_difference_director = list(a_set_director - b_set_director)

				set_difference_based_on = list(a_set_based_on - b_set_based_on)

				set_difference_about = list(a_set_about - b_set_about)

				set_difference_movie_topics = list(a_set_movie_topics - b_set_movie_topics)

				# Finding the set difference b-a

				set_difference_genre1 = list(b_set_genre - a_set_genre)

				set_difference_sub_genre1 = list(b_set_sub_genre - a_set_sub_genre)

				set_difference_director1 = list(b_set_director - a_set_director)

				set_difference_based_on1 = list(b_set_based_on - a_set_based_on)

				set_difference_about1 = list(b_set_about - a_set_about)

				set_difference_movie_topics1 = list(b_set_movie_topics - a_set_movie_topics)

				
				#import pdb;pdb.set_trace()
				if (set_difference_genre):

					a=0
					for element in set_difference_genre:
						
						element_count=0
					
						for movie in Movie_Details.objects.all():
							#if b3 in q.genre.split(','):
							
							if movie.genre:
								movie_genre11=movie.genre.split(',')
								if element in movie_genre11:
									element_count=element_count+1
							else:
								element_count = 0		
							# for sd in movie_genre11:
						try:	
							#print element,"====",element_count
							prob=(element_count*1.0/1103)
							a=a+(math.log(prob,2))
						except ValueError:
							a=0
						
						set_difference_genre0 = a * (-1)
				else:

					set_difference_genre0 = 0 

				#print set_difference_genre0	

				if (set_difference_sub_genre):

					a=0
					for element in set_difference_sub_genre:
						
						element_count=0
					
						for movie in Movie_Details.objects.all():
						#if b3 in q.genre.split(','):
						
							if movie.sub_genre:
								movie_genre11=movie.sub_genre.split(',')
								if element in movie_genre11:
									element_count=element_count+1
						# for sd in movie_genre11:
							
						try:
							#print element,"====",element_count
							prob=(element_count*1.0/1103)
							a=a+math.log(prob,2)
						except ValueError:
							a=0
						
						set_difference_sub_genre0 = a * (-1)
				else:

					set_difference_sub_genre0 = 0 

				#print set_difference_sub_genre0	

				#import pdb;pdb.set_trace()
				
				if (set_difference_director):

					a=0
					for element in set_difference_director:
						
						element_count=0
						for movie in Movie_Details.objects.all():
							#if b3 in q.genre.split(','):
							
							if movie.director:
								movie_genre11=movie.director.split(',')
								if element in movie_genre11:
									element_count=element_count+1

									
							# for sd in movie_genre11:
						try:	
							#print element,"====",element_count
							prob=(element_count*1.0/1103)
							a=a+(math.log(prob,2))
						except ValueError:
							a=0
						
						set_difference_director0 = a * (-1)
				else:

					set_difference_director0 = 0
				


				if (set_difference_based_on):

					a=0
					for element in set_difference_based_on:
						
						element_count=0
					
						for movie in Movie_Details.objects.all():
						#if b3 in q.genre.split(','):
						
							if movie.based_on:
								movie_genre11=movie.based_on.split(',')
								if element in movie_genre11:
									element_count=element_count+1
									
							# for sd in movie_genre11:
						try:	
							#print element,"====",element_count
							prob=(element_count*1.0/1103)
							a=a+(math.log(prob,2))
						except ValueError:
							a=0
						
						set_difference_based_on0 = a * (-1)
				else:

					set_difference_based_on0 = 0 	

				#print set_difference_based_on0

				if (set_difference_about):

					a=0
					for element in set_difference_about:
						
						element_count=0
						for movie in Movie_Details.objects.all():
						#if b3 in q.genre.split(','):
						
							if movie.about:
								movie_genre11=movie.about.split(',')
								if element in movie_genre11:
									element_count=element_count+1
									
							# for sd in movie_genre11:
						try:	
							#print element,"====",element_count
							prob=(element_count*1.0/1103)
							a=a+(math.log(prob,2))
						except ValueError:
							a=0
						
						set_difference_about0 = a * (-1)
				else:

					set_difference_about0 = 0 	

				#print set_difference_about0	

				
				if (set_difference_movie_topics):

					a=0
					for element in set_difference_movie_topics:
						
						element_count=0
					
						for movie in Movie_Details.objects.all():
					
						#if b3 in q.genre.split(','):
						
							if movie.movie_topics_lda:
								movie_genre11=movie.movie_topics_lda.split(', ')
								if element in movie_genre11:
									element_count=element_count+1
									
							# for sd in movie_genre11:
						try:
							#print element,"====",element_count
							prob=(element_count*1.0/1103)
							a=a+(math.log(prob,2))
						except ValueError:
							a=0
						
						set_difference_movie_topics0 = a * (-1)
				else:

					set_difference_movie_topics0 = 0 

				#print set_difference_movie_topics0
				
				
				if (set_difference_genre1):

					a=0
					for element in set_difference_genre1:
						
						element_count=0
						
						for movie in Movie_Details.objects.all():
						#if b3 in q.genre.split(','):
						
							if movie.genre:
								movie_genre11=movie.genre.split(',')
								if element in movie_genre11:
									element_count=element_count+1
									
							# for sd in movie_genre11:
						try:	
							#print element,"====",element_count
							prob=(element_count*1.0/1103)
							a=a+(math.log(prob,2))
						except ValueError:
							a=0
						
						set_difference_genre1 = a * (-1)
				else:

					set_difference_genre1 = 0 

				#print set_difference_genre1	

				if (set_difference_sub_genre1):

					a=0
					for element in set_difference_sub_genre1:
						
						element_count=0
					
						for movie in Movie_Details.objects.all():
						#if b3 in q.genre.split(','):
						
							if movie.sub_genre:
								movie_genre11=movie.sub_genre.split(',')
								if element in movie_genre11:
									element_count=element_count+1
									
							# for sd in movie_genre11:
						try:	
							#print element,"====",element_count
							prob=(element_count*1.0/1103)
							a=a+(math.log(prob,2))
						except ValueError:
							a=0
						
						set_difference_sub_genre1 = a * (-1)
				else:

					set_difference_sub_genre1 = 0 

				#print set_difference_sub_genre1 	
				
				if (set_difference_director1):

					a=0
					for element in set_difference_director1:
						
						element_count=0
						for movie in Movie_Details.objects.all():
							#if b3 in q.genre.split(','):
							
							if movie.director:
								movie_genre11=movie.director.split(',')
								if element in movie_genre11:
									element_count=element_count+1
									
							# for sd in movie_genre11:
						try:	
							#print element,"====",element_count
							prob=(element_count*1.0/1103)
							a=a+(math.log(prob,2))
						except ValueError:
							a=0
						
						set_difference_director1 = a * (-1)
				else:

					set_difference_director1 = 0
				
				#print set_difference_director1	


				if (set_difference_based_on1):

					a=0
					for element in set_difference_based_on1:
						
						element_count=0
						
						for movie in Movie_Details.objects.all():
						#if b3 in q.genre.split(','):
						
							if movie.based_on:
								movie_genre11=movie.based_on.split(',')
								if element in movie_genre11:
									element_count=element_count+1
									
							# for sd in movie_genre11:
						try:	
							#print element,"====",element_count
							prob=(element_count*1.0/1103)
							a=a+(math.log(prob,2))
						except ValueError:
							a=0
						
						set_difference_based_on1 = a * (-1)
				else:

					set_difference_based_on1 = 0 	

				#print set_difference_based_on1

				if (set_difference_about1):

					a=0
					for element in set_difference_about1:
						
						element_count=0
						
						for movie in Movie_Details.objects.all():
						#if b3 in q.genre.split(','):
						
							if movie.about:
								movie_genre11=movie.about.split(',')
								if element in movie_genre11:
									element_count=element_count+1
									
						
							# for sd in movie_genre11:
						try:
							
							#print element,"====",element_count
							prob=(element_count*1.0/1103)
							a=a+(math.log(prob,2))
						except ValueError:
							a=0
						
						set_difference_about1 = a * (-1)
				else:

					set_difference_about1 = 0 	


				#print set_difference_about1

				
				if (set_difference_movie_topics1):

					a=0
					for element in set_difference_movie_topics1:
						
						element_count=0
						
						for movie in Movie_Details.objects.all():
						#if b3 in q.genre.split(','):
						
							if movie.movie_topics_lda:
								movie_genre11=movie.movie_topics_lda.split(', ')
								if element in movie_genre11:
									element_count=element_count+1
									
							# for sd in movie_genre11:
						try:	
							#print element,"====",element_count
							prob=(element_count*1.0/1103)
							a=a+(math.log(prob,2))
						except ValueError:
						
							a=0	
						
						
						set_difference_movie_topics1 = a * (-1)
				else:

					set_difference_movie_topics1 = 0					 	
		        
				#print set_difference_movie_topics1
				
				'''  ## Uncommentt this in case of PICSS_CAMO
				if (set_difference_ab):

					a=0
					for element in set_difference_ab:
						
						element_count=0
						for movie in Movie_Details.objects.all():
							#if b3 in q.genre.split(','):
							
							if not k.movie_topics_lda:
								movie_genre11=movie.movie_topics_lda.split(', ')
								if element in movie_genre11:
									element_count=element_count+1
							# for sd in movie_genre11:
						print element,"====",element_count
						prob=1-(element_count*1.0/1103)
						a=a+(math.log(prob,2))
						
						
						b3_genre = a * (-1)
				else:

					b3_genre = 0 
				'''
				#import pdb;pdb.set_trace()
				
				if (b3):

					a=0
					for element in b3:
						
						element_count=0
						for movie in Movie_Details.objects.all():
						#if b3 in q.genre.split(','):
							movie_genre11=movie.genre.split(',')
							if element in movie_genre11:
								element_count=element_count+1
							# for sd in movie_genre11:
						try:	
							#print element,"====",element_count
							prob=(element_count*1.0/1103)
							a=a+(math.log(prob,2))
						except ValueError:
							a=0
						
						b3_genre = a * (-1)
				else:

					b3_genre = 0 			
				
				
				
				if (b4):

					a=0	

					for element in b4:
						
						element_count=0

						for movie in Movie_Details.objects.all():
						#if b3 in q.genre.split(','):
							movie_genre11=movie.sub_genre.split(',')
							if element in movie_genre11:
								element_count=element_count+1
							# for sd in movie_genre11:
						try:	
							#print element,"====",element_count
							prob=(element_count*1.0/1103)
							a=a+(math.log(prob,2))
						except ValueError:
							a=0
						b4_sub_genre = a * (-1)
				

				else:
					b4_sub_genre = 0
				
				
				
				if (b5):
					a=0
					for element in b5:
					
						element_count=0
						for movie in Movie_Details.objects.all():
							#if b3 in q.genre.split(','):
							movie_genre11=movie.director.split(',')
							if element in movie_genre11:
								element_count=element_count+1
							# for sd in movie_genre11:
						try:	
							#print element,"====",element_count
							prob=(element_count*1.0/1103)
							a=a+(math.log(prob,2))
						except ValueError:
							a=0
						b5_director = a	* (-1)
					
				
				else:
					b5_director = 0

				
				if (b6):	
					a=0
					for element in b6:
						
						element_count=0
						for movie in Movie_Details.objects.all():
							#if b3 in q.genre.split(','):
							movie_genre11=movie.cast.split(',')
							if element in movie_genre11:
								element_count=element_count+1
							# for sd in movie_genre11:
						#print element,"====",element_count
						prob=1-(element_count*1.0/1103)
						a=a+(math.log(prob,2))
						
						b6_cast = a	* (-1)
				else:
					b6_cast = 0
				

				if (b7):			
					a=0
					for element in b7:
						
						element_count=0
						for movie in Movie_Details.objects.all():
						#if b3 in q.genre.split(','):
							movie_genre11=movie.based_on.split(',')
							if element in movie_genre11:
								element_count=element_count+1
							# for sd in movie_genre11:
						try:	
							#print element,"====",element_count
							prob=(element_count*1.0/1103)
							a=a+(math.log(prob,2))
						except ValueError:
							a=0
						b7_based_on = a * (-1)

				else:
					b7_based_on = 0


				if (b8):				
					a=0
					for element in b8:
						
						element_count=0
						for movie in Movie_Details.objects.all():
						#if b3 in q.genre.split(','):
							movie_genre11=movie.about.split(',')
							if element in movie_genre11:
								element_count=element_count+1
							# for sd in movie_genre11:
						try:
							
							#print element,"====",element_count
							prob=(element_count*1.0/1103)
							a=a+(math.log(prob,2))
						except ValueError:
							a=0
						b8_about = a * (-1)

				else:		
					b8_about = 0

				
				if (b10):
					a=0
					for element in b10:
						element_count=0
						for movie in Movie_Details.objects.all():
							if movie.movie_topics_lda:
								movie_genre11=movie.movie_topics_lda.split(', ')
								if  element in movie_genre11:
									element_count=element_count+1
						try:
									
							#print element,"====",element_count			
							prob=(element_count*1.0/1103)
							a=a+(math.log(prob,2))
						except ValueError:
							a=0	
						b10_movie_topics = a * (-1)	

				else:
					b10_movie_topics = 0
				
			    
				aIb = (b3_genre + b4_sub_genre + b7_based_on + b8_about + b10_movie_topics + b5_director + b6_cast) 
				


				a_difference_b = (set_difference_genre0 + set_difference_sub_genre0  + set_difference_based_on0 + set_difference_about0 +set_difference_movie_topics0 + set_difference_director)

				b_difference_a = (set_difference_genre1 + set_difference_sub_genre1 + set_difference_based_on1 + set_difference_about1 +set_difference_movie_topics1 + set_difference_director1)
				
				comparision_paper_sim =  aIb*1.0/(aIb + a_difference_b + b_difference_a )
				feature_dict[k.name.encode('utf-8')] = comparision_paper_sim
				
				print k.id

				print k.name.encode('utf-8')

				print comparision_paper_sim

				print i.name.encode('utf-8')
				print '=================================================================================================='
				
				
		

		import operator
			
		sorted_x = sorted(feature_dict.items(), key=operator.itemgetter(1))
			
			
		for m in Movie_Details.objects.filter(id=moviename):

			

			m.movie_similarity = sorted_x

			m.save()

			print m.id

			print m.name.encode('utf-8')


## Rating Prediction for PICSS_CAMO

	mae=[]
	movie_list_mae = [13] ## Write the name of the Movie ID


    query_list = []
	s=Reviewer_Profile.objects.raw('SELECT id,reviewer_name,reviewer_id, count(reviewer_id) FROM imdbrotten.app_imdb_reviewer_profile group by reviewer_id having count(reviewer_id) between 30 and 50;')
	
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

						sorted_dict = dict(sorted_x[-30:])
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
								user_rating_count = user_rating_count + int(k.movie_ratings[:-3])

						bu = float(user_rating_count)/no_of_movie
								
						if (mu>bu):
							bu = mu - bu
							bu=bu*(-1)
						if (mu<bu):
							bu=bu-mu	

						movie_rat = 0
						count_movie = 0	
						for r in Movie_Details.objects.filter(id=mov):
							'''
							if r.movie_ratings:
								count_movie = count_movie +1
								movie_rat = movie_rat + int(r.movie_ratings[:1])
							'''
							bi = float(r.rating[:-3])	
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

											sim_value = sim_value +value
											
											for bn in Movie_Details.objects.filter(id=key):
												bj = float(bn.rating[:-3])
											if (mu>bj):
												bj = mu - bj
												bj=bj*(-1)
											if (mu<bj):
												bj=bj-mu
											
											total_similarity = total_similarity + (float(k.movie_ratings[:-3]) - (mu + bi + bu)) 
						else:
							count_loop = 1

						if sim_value==0:	
							similarity_score = float(total_similarity)/1
						else:
							similarity_score = float(total_similarity)/sim_value	

						print rw.reviewer_name.encode('utf-8')

						f=open('more_mmta_dbpedia.txt','a')



						#f.write(rw.reviewer_id)

						#f.write('\t')

						f.write(rw.reviewer_name.encode('utf-8'))

						f.write('\t')

						f.write(rw.movie_ratings[:-3])

						f.write('\t')

						differ = float(int(rw.movie_ratings[:-3]) - (mu + bi + bu + similarity_score))

						f.write(str(differ))

						print differ

						print mov

						f.write('\n')

						f.close()
