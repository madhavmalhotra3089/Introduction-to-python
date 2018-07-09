human_langs = ['English', 'French', 'German']

#How many JVM langs do you know ?
print 'I know of ', jvm_langs.__len__()

#It's not a good idea to directly us __xxx__ methods
#A better way is. Remember there is usually a top level function which  
#is the idoimatic way to access the __xxx__method
print 'I know of ', len(human_langs)

print 'Oops I forgot Clojure'
jvm_langs.append('Russian')

#Let's iterate across the list
for lang in human_langs:
  print lang
  
#Can we get the 3rd element of the list ?
print "The 3rd human language is ", human_langs[2]
print "The first 3 human languages are ", human_langs[:3]
print "The 2nd to 4th human languages are ", human_langs[1:4]

print "let's sort these languages"
human_langs.sort()
print human_langs