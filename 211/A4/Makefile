JC = javac
JAVA = java
VIEWER = more
FILES = \
	EmailService.java \
	PhoneService.java \
	VoiceService.java \
	ServiceNotifier.java \
	Service.java \
	DecisionEngine.java 
	
MAIN = DecisionEngine

.PHONY: run clean view


run: $(FILES)
	@$(JC) $(FILES)
	$(JAVA) $(MAIN)

view: $(FILES) README
	$(VIEWER) README
	$(VIEWER) $(FILES)


clean:
	- rm *.class


