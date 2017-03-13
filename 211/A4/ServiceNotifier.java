import java.util.*;

public class ServiceNotifier{
	
	//Array of Current Survices	
	ArrayList<Service> _services = new ArrayList<>();

	public void attach(Service pService){
		//Add passed in Service to Current Array
		_services.add(pService);	
	}


	public void detach(Service pService){
		//Remove service and set message to None
		pService.update("None");
		_services.remove(pService);
		
	}


	public void notify(String message){
		//For each service in array of services
		//update their message
		for(Service service : _services){
			service.update(message);
		}
	}


}
