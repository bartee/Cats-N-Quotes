/**
 * Created with PyCharm.
 * User: bartstroeken
 * Date: 7/27/13
 * Time: 8:33 AM
 * To change this template use File | Settings | File Templates.
 */
function stopAnimation(){

    random_number = Math.random();
    if (random_number < 0.9){
        // Doesn't work on Firefox, but still handy nonetheless
        window.stop();
    }

}

$(function(){
    now = new Date();

    // Time based
    // It's weekend!
    is_weekend = (now.getDay() == 6 || now.getDay() ==0) ? true : false;
    if (is_weekend){

        return;
    }
    if ((now.getHours() > 9 && now.getHours() <12) || (now.getHours()>13 && now.getHours < 17)){
        stopAnimation();
    }

});