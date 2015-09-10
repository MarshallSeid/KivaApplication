
        function queryHDI(callback) {
            $.ajax({
                type: "GET",
                url: "http://data.undp.org/resource/myer-egms.json?country=" + countryName, 
                success: function(response, data) {
                    // Run the code here that needs to access the data returned
                    console.log("QUERY POINTS WAS A SUCCESS");
                    console.log("RESPONSE: " + response);
                    console.log("DATA: " + data);
                    console.log("HDI RANK: " + response[0]["hdi_rank"]);
                    //var obj = JSON.parse(response);
                    //console.log("OBJECT: " + obj);
                    var r = buildHDIArray(response);
                    console.log("Result of buildHDIArray: " + r);
                    return callback(null, r);
                },
                error: function(response, data) {
                    console.log("Error in Query: " + response);
                    console.log("Data from ERROR: " + data);
                    alert('Error occured');
                },
               dataType: "json"
            });
        };

         function buildHDIArray(json) {  
            console.log("-------HERE 2"); 
            var hdiIndexArr= [];
            var arr = [];
            for (i = 0; i < json.length; i++) { 
                hdiIndexArr.push(json[0]["hdi_rank"]); // {'lat': json[i]['location']['latitude'], 'lon': json[i]['location']['longitude']});
            }
            console.log(hdiIndexArr);
            return hdiIndexArr;
        };



 // Headmap for San Diego
        function getUKPoints(dataMap) {
            console.log("Hits getUKPoints");
            var returnArray = [];
            console.log("DATA MAP: " + dataMap);
            for(i = 0; i < dataMap.length; i++) {
                returnArray.push(new google.maps.LatLng(dataMap[i]['lat'], dataMap[i]['lon']));    
            }
            console.log("RETURN ARRAY: " + returnArray);
            return returnArray;
        }