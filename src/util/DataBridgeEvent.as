package util{
    import flash.events.Event;

    public class DataBridgeEvent extends Event {
        
        public var data:String;

        public function DataBridgeEvent(type:String, bubbles:Boolean = true, cancelable:Boolean = false) {
            super(type, bubbles, cancelable);
        }

        public override function clone():Event {
            // 1. Create the new event instance
            var clonedEvent:DataBridgeEvent = new DataBridgeEvent(type, bubbles, cancelable);
            // 2. Explicitly copy your string data over before returning it!
            clonedEvent.data = this.data; 
            return clonedEvent;
        }
    }
}
