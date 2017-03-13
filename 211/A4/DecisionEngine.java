import java.util.*;
import java.lang.*;

public class DecisionEngine{
	
	//Create engine as a Singleton	
	public static DecisionEngine engine = new DecisionEngine();
	
	public DecisionEngine(){}

	public static DecisionEngine getInstance() {
		return engine;
	}

	public static String weatherInfo(){

		/*Get Weather Data pulled from some resource
		Return status of message sent based on data*/
		
		String weatherMessage;
		String poss1, poss2, poss3;
		String weatherInfo;

		poss1 = "Severe";
		poss2 = "Delay";
		poss3 = "Normal";

		//return Delay for this case; set to whatever info is generated.
		weatherInfo = poss2;

		if("Severe".equals(weatherInfo)){
			weatherMessage = "ALL CLASS CANCELED FOR TOMORROW";
			}
		else if("Delay".equals(weatherInfo)){
			weatherMessage = "2 HOUR DELAY";
			}
		else{
			weatherMessage = "OPERATING SCHEDULE AS NORMAL";
			}

		return weatherMessage;

	}

	public static void main(String [] args){
	
	//Create Service Objects
	PhoneService phoneHandler = new PhoneService();
	EmailService emailHandler = new EmailService();
	VoiceService voiceHandler = new VoiceService();

	//Create a Service Notifier
	ServiceNotifier notifySystem = new ServiceNotifier();
	
	//Obtain message from DecisionEngine
	String message;
	DecisionEngine decision = DecisionEngine.getInstance();

	/*If new method needs to added all have to do is make sure follows Service interface
	and is added to the notifying system*/
	
	//Attach each System to the ServiceNotifier
	notifySystem.attach(phoneHandler);
	notifySystem.attach(emailHandler);
	notifySystem.attach(voiceHandler);

	message = decision.weatherInfo();

	//Update the message to the Notifying System.
	notifySystem.notify(message);

	System.out.println("");
		
	//Check status of Service Objects
	System.out.println(phoneHandler);	
	System.out.println(emailHandler);	
	System.out.println(voiceHandler);

	System.out.println("");
	
	//Detach a service
	notifySystem.detach(voiceHandler);

	//Recheck status of handlers
	System.out.println(phoneHandler);	
	System.out.println(emailHandler);	
	System.out.println(voiceHandler);

	System.out.println("");
	}

}
