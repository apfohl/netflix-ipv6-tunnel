def init(id, cfg):
  return True

def deinit(id):
  return True

def inform_super(id, qstate, superqstate, qdata):
  return True

def operate(id, event, qstate, qdata):
  if event == MODULE_EVENT_NEW:
    if qstate.qinfo.qtype == RR_TYPE_AAAA:
      if qstate.qinfo.qname_str.endswith('netflix.com.') or qstate.qinfo.qname_str.endswith('nflximg.com.'):
        msg = DNSMessage(qstate.qinfo.qname_str, RR_TYPE_A, RR_CLASS_IN, PKT_QR | PKT_RA | PKT_AA)

        if not msg.set_return_msg(qstate):
          qstate.ext_state[id] = MODULE_ERROR
          return True

        qstate.return_msg.rep.security = 2
        qstate.return_rcode = RCODE_NOERROR
        qstate.ext_state[id] = MODULE_FINISHED

        return True

    qstate.ext_state[id] = MODULE_WAIT_MODULE

    return True

  if event == MODULE_EVENT_MODDONE:
    qstate.ext_state[id] = MODULE_FINISHED

    return True
