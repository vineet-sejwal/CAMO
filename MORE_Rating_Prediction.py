def more_paper_camo(request):

	

	import math
	feature_dict={}	
	movie_list =[]
	
	import itertools as it
	
	movie_list = [14,15] #movie ids for which you need to compute similarity based on MORE


	for moviename in movie_list:
		a_list_genre = []

		a_list_sub_genre =[]

		a_list_director =[]

		a_list_based_on=[]

		a_list_about =[]

		a_list_movie_topics =[]

		movie_1_vector = []

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
			a_set_genre = set([item for sublist in a_list_genre for item in sublist])
			a_set_genre = list(a_set_genre)
			a_set_sub_genre = set([item for sublist in a_list_sub_genre for item in sublist])
			a_set_sub_genre = list(a_set_sub_genre)
			a_set_director = set([item for sublist in a_list_director for item in sublist])
			a_set_director = list(a_set_director)
			a_set_based_on = set([item for sublist in a_list_based_on for item in sublist])
			a_set_based_on = list(a_set_based_on)
			a_set_about = set([item for sublist in a_list_about for item in sublist])
			a_set_about = list(a_set_about)
			a_set_movie_topics = set([item for sublist in a_list_movie_topics for item in sublist])
			a_set_movie_topics = list(a_set_movie_topics)

			if (a_set_genre):

				a=0
				for element in a_set_genre:
					
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

			movie_1_vector.append(set_difference_genre0)

			#print set_difference_genre0	

			if (a_set_sub_genre):

				a=0
				for element in a_set_sub_genre:
					
					element_count=0
					
					for movie in Movie_Details.objects.all():
						#if b3 in q.genre.split(','):
						
						if movie.sub_genre:
							movie_genre11=movie.sub_genre.split(',')
							if element in movie_genre11:
								element_count=element_count+1
						else:
							element_count = 0		
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

			
			movie_1_vector.append(set_difference_sub_genre0)
			
			if (a_set_director):

				a=0
				for element in a_set_director:
					
					element_count=0

					for movie in Movie_Details.objects.all():
						#if b3 in q.genre.split(','):
						
						if movie.director:
							movie_genre11=movie.director.split(',')
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
					
					set_difference_director0 = a * (-1)
			else:

				set_difference_director0 = 0
			

			#print set_difference_director0	
			movie_1_vector.append(set_difference_director0)

			if (a_set_based_on):

				a=0
				for element in a_set_based_on:
					
					element_count=0
					
					for movie in Movie_Details.objects.all():
						#if b3 in q.genre.split(','):
						
						if movie.based_on:
							movie_genre11=movie.based_on.split(',')
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
					
					set_difference_based_on0 = a * (-1)
			else:

				set_difference_based_on0 = 0 	

			#print set_difference_based_on0
			movie_1_vector.append(set_difference_based_on0)
			if (a_set_about):

				a=0
				for element in a_set_about:
					
					element_count=0
					
					for movie in Movie_Details.objects.all():
						#if b3 in q.genre.split(','):
						
						if movie.about:
							movie_genre11=movie.about.split(',')
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
					
					set_difference_about0 = a * (-1)
			else:

				set_difference_about0 = 0 	

			#print set_difference_about0	
			movie_1_vector.append(set_difference_about0)
			''' ## If you want MORE to be used with full CAMO uncomment this and used it 

			if (a_set_movie_topics):

				a=0
				for element in a_set_movie_topics:
					
					element_count=0
					
					for movie in Movie_Details.objects.all():
					
						#if b3 in q.genre.split(','):
						
						if movie.movie_topics_lda:
							movie_genre11=movie.movie_topics_lda.split(', ')
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
					
					set_difference_movie_topics0 = a * (-1)
			else:

				set_difference_movie_topics0 = 0 

			movie_1_vector.append(set_difference_movie_topics0)
			'''
			
			
			

			for k in Movie_Details.objects.filter(id=new_range):

				b_list_genre = []

				b_list_sub_genre =[]

				b_list_director =[]

				b_list_based_on=[]

				b_list_about =[]

				b_list_movie_topics =[]

				movie_2_vector = []

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

				
			
				#import pdb;pdb.set_trace()
				
				b_set_genre = set([item for sublist in b_list_genre for item in sublist])
				b_set_genre = list(b_set_genre)
				b_set_sub_genre = set([item for sublist in b_list_sub_genre for item in sublist])
				b_set_sub_genre = list(b_set_sub_genre)
				b_set_director = set([item for sublist in b_list_director for item in sublist])
				b_set_director = list(b_set_director)
				b_set_based_on = set([item for sublist in b_list_based_on for item in sublist])
				b_set_based_on = list(b_set_based_on)
				b_set_about = set([item for sublist in b_list_about for item in sublist])
				b_set_about = list(b_set_about)
				b_set_movie_topics = set([item for sublist in b_list_movie_topics for item in sublist])
				b_set_movie_topics = list(b_set_movie_topics)

				# Finding the set difference a-b

				
				#import pdb;pdb.set_trace()
					

				#print set_difference_movie_topics0
				if (b_set_genre):

					a=0
					for element in b_set_genre:
						
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
						
						set_difference_genre1 = a * (-1)
				else:

					set_difference_genre1 = 0 

				#import pdb;pdb.set_trace()
				movie_2_vector.append(set_difference_genre1)
				#print set_difference_genre0	

				if (b_set_sub_genre):

					a=0
					for element in b_set_sub_genre:
						
						element_count=0
					
						for movie in Movie_Details.objects.all():
								#if b3 in q.genre.split(','):
								
							if movie.sub_genre:
								movie_genre11=movie.sub_genre.split(',')
								if element in movie_genre11:
									element_count=element_count+1
							else:
								element_count = 0		
							# for sd in movie_genre11:
							
						try:
							#print element,"====",element_count
							prob=(element_count*1.0/1103)
							a=a+math.log(prob,2)
						except ValueError:
							a=0
						
						set_difference_sub_genre1 = a * (-1)
				else:

					set_difference_sub_genre1 = 0 

				#print set_difference_sub_genre0	
				movie_2_vector.append(set_difference_sub_genre1)
				#import pdb;pdb.set_trace()
				
				if (b_set_director):

					a=0
					for element in b_set_director:
						
						element_count=0
						
						for movie in Movie_Details.objects.all():
							#if b3 in q.genre.split(','):
							
							if movie.director:
								movie_genre11=movie.director.split(',')
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
						
						set_difference_director1 = a * (-1)
				else:

					set_difference_director1 = 0
				
				movie_2_vector.append(set_difference_director1)
				#print set_difference_director0	


				if (b_set_based_on):

					a=0
					for element in b_set_based_on:
						
						element_count=0
						
						for movie in Movie_Details.objects.all():
							#if b3 in q.genre.split(','):
							
							if movie.based_on:
								movie_genre11=movie.based_on.split(',')
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
						
						set_difference_based_on1 = a * (-1)
				else:

					set_difference_based_on1 = 0 	

				#print set_difference_based_on0
				movie_2_vector.append(set_difference_based_on1)

				if (b_set_about):

					a=0
					for element in b_set_about:
						
						element_count=0
						
						for movie in Movie_Details.objects.all():
							#if b3 in q.genre.split(','):
							
							if movie.about:
								movie_genre11=movie.about.split(',')
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
						
						set_difference_about1 = a * (-1)
				else:

					set_difference_about1 = 0 	

				#print set_difference_about0	
				movie_2_vector.append(set_difference_about1)
				''' Uncomment this to use MORE with CAMO 
				if (b_set_movie_topics):

					a=0
					for element in b_set_movie_topics:
						
						element_count=0
						for st in it.chain(range(6,106), range(358,458), range(786,886)):
							for movie in Movie_Details.objects.filter(id=st):
						
							#if b3 in q.genre.split(','):
							
								if movie.movie_topics_lda:
									movie_genre11=movie.movie_topics_lda.split(', ')
									if element in movie_genre11:
										element_count=element_count+1
								else:
									element_count = 0		
									
							# for sd in movie_genre11:
						try:
							#print element,"====",element_count
							prob=(element_count*1.0/300)
							a=a+(math.log(prob,2))
						except ValueError:
							a=0
						
						set_difference_movie_topics1 = a * (-1)
				else:

					set_difference_movie_topics1 = 0 

				movie_2_vector.append(set_difference_movie_topics1)
				'''
				from numpy import dot
				from numpy.linalg import norm
				from scipy import spatial
				#cos_sim = dot(movie_1_vector, movie_2_vector)/(norm(movie_1_vector)*norm(movie_2_vector))
				cos_sim = 1 - spatial.distance.cosine(movie_1_vector, movie_2_vector)
				
				feature_dict[k.name.encode('utf-8')] = cos_sim
				
				print k.id

				print k.name.encode('utf-8')

				print cos_sim

				print i.name.encode('utf-8')
				#import pdb;pdb.set_trace()
				print '=================================================================================================='
			
				
		

		import operator
			
		sorted_x = sorted(feature_dict.items(), key=operator.itemgetter(1))
			
			
		for m in Movie_Details.objects.filter(id=moviename):

			

			m.movie_similarity_pearson_correlation = sorted_x

			m.save()

			print m.id

			print m.name.encode('utf-8')

	## Rating Prediction using MORE
	
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