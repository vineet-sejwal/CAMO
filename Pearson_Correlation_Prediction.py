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


def pearsoncorrelation(request):
	
	list1=[]
	list2=[]
	feature_dict={}
	movie_list=[]

	for kk in range(1,1103):
		movie_list.append(kk)

	
	new_list=[]
	mlist=[]
	for moviename in movie_list:
	
		for m in Movie_Details.objects.filter(id=moviename):
			reviewer_list_m=[]
			
			result_set_m=Reviewer_Profile.objects.raw('SELECT id,reviewer_name,reviewer_id from moviedb2.app_imdb_Reviewer_Profile where movie_name_id=' +str(m.id)+ ';')	

			for reviewer_id_m in result_set_m:
				reviewer_list_m.append(reviewer_id_m.reviewer_id)

			for mm in range(1,1103):

				mlist.append(mm)	

			for s in mlist:
				for m1 in Movie_Details.objects.filter(id=s):
					reviewer_list_m1=[]
					result_set_m1=Reviewer_Profile.objects.raw('SELECT id,reviewer_name,reviewer_id from moviedb2.app_imdb_Reviewer_Profile where movie_name_id=' +str(m1.id)+ ';')

					for reviewer_name_m1 in result_set_m1:
						reviewer_list_m1.append(reviewer_name_m1.reviewer_id)
					if m.id!=m1.id:
						list3= list(set(reviewer_list_m).intersection(reviewer_list_m1))	
						print list3
					else:
						list3=[]
					

					total_sum=0
					count=0		
					for kl in Reviewer_Profile.objects.filter(movie_name_id=m.id):
						
						if kl.movie_ratings:
							count=count+1
							total_sum=total_sum+int(kl.movie_ratings[:-3])

					try:		

						average=float(total_sum*1.0/count)
					except ZeroDivisionError:
						average =0


					average2=average

					total_sum1=0
					count1=0

					for kl1 in Reviewer_Profile.objects.filter(movie_name_id=m1.id):
						if kl1.movie_ratings:
							#print kl1.movie_ratings[:-3]
							count1=count1+1
							total_sum1=total_sum1+int(kl1.movie_ratings[:-3])
						
						
					
						
					try:
						average1 = float(total_sum1*1.0/count1)

					except ZeroDivisionError:

						average1 = 0	

					average3 = average1
					
					print len(list3)
					counter_loop=len(list3)
					total_sum_value=0
					sqrt1 =0
					sqrt2 =0
					for k in list3:
						
						for a in Reviewer_Profile.objects.filter(reviewer_id__icontains=k):
							if a.movie_name_id==m.id:
								counter_loop=counter_loop-1
								print counter_loop
								if a.movie_ratings:

									for kq in Reviewer_Profile.objects.filter(reviewer_id__icontains=k):
						
										if kq.movie_name_id==m1.id:
											if kq.movie_ratings:
												

												
												sqrt1 = sqrt1 + math.pow((float(a.movie_ratings[:-3])-average),2)
												sqrt2 = sqrt2 + math.pow((float(kq.movie_ratings[:-3])-average1),2)
													
												
					sqrt1 = math.sqrt(sqrt1)
					sqrt2 = math.sqrt(sqrt2)
					print sqrt1
					print sqrt2							
					
					for k in list3:
						
						
						for a in Reviewer_Profile.objects.filter(reviewer_id__icontains=k):
							if a.movie_name_id==m.id:
								if a.movie_ratings:
									#print a.reviewer_name
									print a.reviewer_id
									print a.movie_ratings
									first = int(a.movie_ratings[:-3])
									print a.movie_name_id
								else:
									first = 0
									average =0	

						for kq in Reviewer_Profile.objects.filter(reviewer_id__icontains=k):
						
							if kq.movie_name_id==m1.id:
								if kq.movie_ratings:
									#print kq.reviewer_name
									print kq.reviewer_id
									print kq.movie_ratings
									second = int(kq.movie_ratings[:-3])
									print kq.movie_name_id	

								else:
									second = 0	
									average1=0	
						
							
							
						#import pdb;pdb.set_trace()	
						total_sum_value = total_sum_value + (first-average)*(second-average1)
						
						average=average2
						average1=average3
						print "=========================================================================="
				
					if (sqrt1==0 or sqrt2==0):
						corelation_similarity=1
					else:
						corelation_similarity =  total_sum_value*1.0/((sqrt1)*(sqrt2))	

					feature_dict[m1.name.encode('utf-8')] = corelation_similarity
					f=open('pearson_rel_25.txt','a')

					f.write(m1.name.encode('utf-8'))

					f.write(str(corelation_similarity))	

			import operator
				
			sorted_x = sorted(feature_dict.items(), key=operator.itemgetter(1))
				
				
			for m in Movie_Details.objects.filter(id=moviename):

				

				m.movie_similarity_pearson_correlation = sorted_x

				m.save()

				print m.id

				print m.name.encode('utf-8')


def perasoncorrelationprediction(request):

	
	from ast import literal_eval as make_tuple
	query_list = []
	mae=[]
	movie_list_mae = [10]
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

							new_dict=((i.movie_similarity_pearson_correlation))
							
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

						


						total_similarity=0
						count_loop = 0
						sim_value = 0
						if flat_lis:
							for key, value in flat_lis.iteritems():
							
							
								for k in Reviewer_Profile.objects.filter(reviewer_id__icontains=q):

									if k.movie_ratings:

										if (key == k.movie_name_id):

											

											sim_value = sim_value + (value)


											total_similarity = total_similarity + (float(k.movie_ratings[:-3]) * float (value)) 
						else:
							count_loop = 1

						if sim_value==0:	
							similarity_score = float(total_similarity)/1
						else:
							similarity_score = float(total_similarity)/sim_value	

						print rw.reviewer_name

						f=open('mean_absolute_error_gcss_10.txt','a')

						f.write(rw.reviewer_name)

						f.write('\t')

						f.write(rw.movie_ratings)

						f.write('\t')

						differ = float(int(rw.movie_ratings[:-3]) - (similarity_score))

						f.write(str(differ))

						print differ

						f.write('\n')

						f.close()				