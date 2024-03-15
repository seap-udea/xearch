##################################################################
#BASIC RULES
##################################################################
clean:cleancrap

cleanall:cleancrap

#=========================
#Clean
#=========================
cleancrap:
	@echo "Cleaning crap..."
	@-find . -name "*~" -delete
	@-find . -name "desktop.ini" -delete
	@-find . -name "#*#" -delete
	@-find . -name "#*" -delete
	@-find . -name ".#*" -delete
	@-find . -name ".#*#" -delete
	@-find . -name ".DS_Store" -delete
	@-find . -name "Icon*" -delete
	@-find . -name "*.egg-info*" -type d | xargs rm -fr
	@-find . -name "*.pyc" -delete

#=========================
#Clean
#=========================
signals:
	@-rm -rf public/signals/*
	@-cp -rf signals/* public/signals
	@-zip signals.zip -r signals