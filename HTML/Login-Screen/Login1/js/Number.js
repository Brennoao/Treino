function onlynumber(evt) {
    var theEvent = evt || window.event
    var key = theEvent.keyCode || theEvent.whidth
    key = String.fromCharCode( key )
    // var regex = /^[0-9.,]+$/
    var regex = /^[0-9.]+$/
    if (!regex.test( key ) ) {
        theEvent.returnValue = false;
        if(theEvent.preventDefault) theEvent.preventDefault()
    }
}

function onlynumberN (evt) {
    var theEvent = evt || window.event
    var key = theEvent.keyCode || theEvent.whidth
    key = String.fromCharCode( key )
    // var regex = /^[0-9.,]+$/
    var regex = /^[0-9 /]+$/
    if (!regex.test( key ) ) {
        theEvent.returnValue = false;
        if(theEvent.preventDefault) theEvent.preventDefault()
    }
}

function onlynumberT (evt) {
    var theEvent = evt || window.event
    var key = theEvent.keyCode || theEvent.whidth
    key = String.fromCharCode( key )
    // var regex = /^[0-9.,]+$/
    var regex = /^[0-9 () -]+$/
    if (!regex.test( key ) ) {
        theEvent.returnValue = false;
        if(theEvent.preventDefault) theEvent.preventDefault()
    }
}