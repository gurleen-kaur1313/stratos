var i = 1;

let announcement = document.getElementById("announce");
const proxyurl = "https://cors-anywhere.herokuapp.com/";
fetch(proxyurl + "http://stratos-backend.herokuapp.com/graphql/", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IndoeXdoeUB3aHkuY29tIiwiZXhwIjoxNjE0NDY2OTY3LCJvcmlnSWF0IjoxNjE0NDY2NjY3fQ.QWjUeO2FcmzF4bZbq-Ibr_l0kage3Cf-2Tl2VeL7cqQ"

        },
        body: JSON.stringify({
            query: `query
            {
                getAllTest
                {
                  user
                  {
                    name
                    mobile
                    state
                    city
                  }
                }
            }
        `
        })
    }).then(res => res.json())
    .then(data => {
        console.log(data.data.getAllTest);
        data.data.getAllTest.forEach(getAllTest => {

            document.getElementById("info").innerHTML += `<tr>
        <th scope="row">${i}</th>
        <td>${getAllTest.user.name}</td>
        <td>${getAllTest.user.mobile}</td>
        <td>${getAllTest.user.city}, ${getAllTest.user.state}</td>
        <td>Unhealthy</td>
        <td><a href="mailto:test1@abc.com"><button class="btn btn-danger" >Message</button></td></form>
        </tr>`
            i++;

        });

    });