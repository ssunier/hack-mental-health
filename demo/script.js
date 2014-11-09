

        

// JavaScript Document
var main = function(){
	$('#share').click(function(){
        $(this).toggleClass('buttonclick')
        $(this).delay( 300 ).queue(function(next){$(this).removeClass('buttonclick');next();})
})
	$('#compare').click(function(){
        $(this).toggleClass('buttonclick')
        $(this).delay( 300 ).queue(function(next){$(this).removeClass('buttonclick');next();})
})
	
	var x = [0,0,0,0,0,0,0,0,0,0];
	var y = [0,0,0,0,0,0,0,0,0,0];


	
	$('.xdat').click(function(){
		//$('.xdat_select').removeClass('xdat_select');
		var varID = jQuery(this).attr("id");
		
		$('.xdatselect').removeClass('xdatselect');
		$(this).addClass('xdatselect');
		
		switch(varID){
			case 'xexcercise':
				x = $( "#xexcercise" ).data()['data'];
				break;
			case 'xmood':
				x = $( "#xmood" ).data()['data'];
				x = $( "#xmood" ).data()['data'];
				break;
			case 'xsleep':
				x = $( "#xsleep" ).data()['data'];
				x = $( "#xsleep" ).data()['data'];
				break;
			case 'xbrowse':
				x = $( "#xbrowse" ).data()['data'];
				x = $( "#xbrowse" ).data()['data'];
				break;
		}
            plotdata=[]
            for (var i=0; i<x.length;i++){
                plotdata.push([x[i],y[i]])
            }
		plot(plotdata)
		
		})
	
	$('.ydat').click(function(){
		$('.ydatselect').removeClass('ydatselect');
		$(this).addClass('ydatselect');
		var varID = jQuery(this).attr("id");
		
		switch(varID){
			case 'yexcercise':
				y = $( "#yexcercise" ).data()['data'];
//                        $('p').text(y)
				break;
			case 'ymood':
				y = $( "#ymood" ).data()['data'];
				break;
			case 'ysleep':
				y = $( "#ysleep" ).data()['data'];
				break;
			case 'ybrowse':
				y = $( "#ybrowse" ).data()['data'];
				break;
		}
            plotdata=[]
            for (var i=0; i<x.length;i++){
                plotdata.push([x[i],y[i]])
            }
		plot(plotdata)
		})
	
            //var randdata=genDat(30,20); //return [randarray,anticorr,poscorr,randarray2]


     
	
	
	/* ----------------------------------------------------------------*/
	var plot = function(plotdata){
        $('#container').highcharts({
            chart: {
                type: 'scatter'
            },
            title: {
                text: 'Health Correlations'
            },
            series: [{color: 'rgba(212, 76, 155, 1)',
                data: plotdata
            }],
            legend:{enabled:0},
            plotOptions: {
                        scatter: {
                            marker: {
                                radius: 5,
                                states: {
                                    hover: {
                                        enabled: true,
                                        lineColor: 'rgb(100,100,100)'
                                    }
                                }
                            },
                            states: {
                                hover: {
                                    marker: {
                                        enabled: false
                                    }
                                }
                            }}}
    		});
	}


randarray=[];
anticorr=[];
poscorr=[];
randarray2=[];
size=50;
for (var i = 0; i< size; i++){
    noise = 100;
    randnum=Math.round(Math.random() * 500) + Math.random()*noise;
    smallrandnum=Math.round(Math.random() * 100) + Math.random()*noise;
    randnum2=Math.round(Math.random() * 500) + Math.random()*noise;
    randarray.push(randnum);
    randarray2.push(randnum2);
    poscorr.push(smallrandnum+randnum + Math.random()*noise);
    anticorr.push(smallrandnum-randnum+1000 + Math.random()*noise)
    }

$('#yexcercise').data({data:randarray});
$('#xexcercise').data({data:randarray});

$('#ymood').data({data:poscorr});
$('#xmood').data({data:poscorr});

$('#ysleep').data({data:randarray2});
$('#xsleep').data({data:randarray2});

$('#ybrowse').data({data:anticorr});
$('#xbrowse').data({data:anticorr});

/* PREDICTIVE --------------------------------------------------------------
variables
*/
    var good_mood_tm = [70, 80, 90]
    var poor_mood_tm = [10, 20, 30]
    
    var event_nm = ["good_sleep", 
    "poor_sleep", 
    "good_exercise", 
    "poor_exercise",
    "poor_browsing",
    "good_browsing"];
    
    var event_tm = [[25, 55, 64, 72, 80],
    [12, 24, 36, 40, 45],
    [45, 47, 49, 68, 70, 72],
    [16, 18, 20],
    [19, 39, 59, 79],
    [15, 35, 55, 75]];


	$('#syncbutton').click(function(){
            


		$(this).addClass('buttonclick');
            predict(good_mood_tm,poor_mood_tm,event_nm,event_tm);
            good_mood_tm.push(Math.floor((Math.random() * 100) + 1));
            poor_mood_tm.push(Math.floor((Math.random() * 100) + 1));
            for (var i = 0; i < event_tm.length; i++) {
                event_tm[i].push(Math.floor((Math.random() * 100) + 1));
                }

        	  $(this).delay( 300 ).queue(function(next){$(this).removeClass('buttonclick');next();})

        }
        )

};


/* PREDICTIVE --------------------------------------------------------------------------------
*/

var predict=function (good_mood_tm,poor_mood_tm,event_nm,event_tm) {
    var score = [];
    
    for (var i = 0; i < event_nm.length; i++) {
    var gms = 0, pms = 0;
    
    for (var j = 0; j < event_tm[i].length; j++) {
    for (var k = 0; k < good_mood_tm.length; k++) {
    if (event_tm[i][j] < good_mood_tm[k]) {
    gms += 100 / (good_mood_tm[k] - event_tm[i][j]);
    }
    }
    
    for (var k = 0; k < poor_mood_tm.length; k++) {
    if (event_tm[i][j] < poor_mood_tm[k]) {
    pms += 100 / (poor_mood_tm[k] - event_tm[i][j]);
    }
    }
    }
    
    score.push([gms / (gms + pms + 1e-6), event_nm[i]]);
    }
    
    score.sort().reverse(); var res = "";
    //score: [[score,activity],[score,activity]...]
    for (var j = 0; j<score.length; j++) {
    	$('#p'+j).text(score[j][1])
    	if (score[j][0]<.40){
    		$('#p'+j).css('background-color','#D44C9B');
    		$('#p'+j).css('color','#FFFFFF');
    	} else if (score[j][0]<.60) {
    		$('#p'+j).css('background-color','#FFFFFF');
    		$('#p'+j).css('color','#BBBDC0');
    	} else {
    		$('#p'+j).css('background-color','#4CD3D3');
    		$('#p'+j).css('color','#FFFFFF');
    	}
    	/*
    	var activity = score[j][1] //activity
    	switch (activity) {
    		case "good_sleep":
    			$('#p1').data(score[j][0]); //score
    			break;
    		case "poor_sleep":
    			$('#p2').data(score[j][0]); //score
    			break;
    		case "good_exercise":
    			$('#gexercise').data(score[j][0]); //score
    			break;
    		case "poor_exercise":
    			$('#pexercise').data(score[j][0]); //score
    			break;
    		case "good_browsing":
    			$('#gbrowse').data(score[j][0]); //score
    			break;
    		case "poor_browsing":
    			$('#pbrowse').data(score[j][0]); //score
    			break;
    		}*/
    }
    
    for (var i = 0; i < score.length; i++) {
    res += score[i][1] + ":" + score[i][0] + "\n";
}}







$(document).ready(main);