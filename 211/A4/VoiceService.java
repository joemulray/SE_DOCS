public class VoiceService implements Service{
	
	String message;
	
	public void update(String message){
		/* Open file containing all users registered for voice
	     	notification. Open connection to the Voice server.
	    	For all registered clients, notify them via voice message. */	
		this.message = message;
		System.out.println("NOTIFYING USERS BY VOICE");

	}
	
	public String toString(){
	
	//toString method to check status of Voice message	
	String str = "VoiceService Message: " + message ;
	return str;
	
	}

}
