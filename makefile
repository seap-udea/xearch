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
packsignals:
	@-rm -rf public/signals/*
	@-cp -rf dev/signals/* public/signals
	@-rm -rf signals.zip
	@-cd public;zip -FSq ../signals.zip -r signals
	@-cp signals.zip ../xearch-repo/
