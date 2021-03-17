using Microsoft.Web.WebSockets;
using System.Net;
using System.Net.Http;
using System.Web;
using System.Web.Http;

namespace ChatServer2.Controllers
{
    public class EngineControlController : ApiController
    {
        public HttpResponseMessage Get(string clientId)
        {
            HttpContext.Current.AcceptWebSocketRequest(new EngineControlWebSocketHandler(clientId));
            return Request.CreateResponse(HttpStatusCode.SwitchingProtocols);
        }

        public IHttpActionResult Get()
        {            
            return Ok(EngineControlWebSocketHandler._engineControlClients.Count);
        }
    }

    class EngineControlWebSocketHandler : WebSocketHandler
    {
        public static WebSocketCollection _engineControlClients = new WebSocketCollection();
        private string _clientId;

        public EngineControlWebSocketHandler(string clientId)
        {
            _clientId = clientId;
        }

        public override void OnOpen()
        {
            _engineControlClients.Add(this);
        }

        public override void OnMessage(string message)
        {
            _engineControlClients.Broadcast(message);            
        }
    }
}
