import{S as G,i as J,s as M,F as N,c as T,m as L,t as v,a as y,d as z,C as R,E as U,g as _,k as W,n as Y,o as b,G as j,p as A,q as B,e as m,w as C,b as h,f as d,r as F,h as k,u as q,v as D,y as E,x as I,z as H}from"./index.994990a4.js";function K(r){let e,t,s,l,n,o,c,a,i,u,g,$,p=r[3]&&S(r);return o=new B({props:{class:"form-field required",name:"password",$$slots:{default:[Q,({uniqueId:f})=>({8:f}),({uniqueId:f})=>f?256:0]},$$scope:{ctx:r}}}),{c(){e=m("form"),t=m("div"),s=m("h5"),l=C(`Type your password to confirm changing your email address
                    `),p&&p.c(),n=h(),T(o.$$.fragment),c=h(),a=m("button"),i=m("span"),i.textContent="Confirm new email",d(t,"class","content txt-center m-b-base"),d(i,"class","txt"),d(a,"type","submit"),d(a,"class","btn btn-lg btn-block"),a.disabled=r[1],F(a,"btn-loading",r[1])},m(f,w){_(f,e,w),k(e,t),k(t,s),k(s,l),p&&p.m(s,null),k(e,n),L(o,e,null),k(e,c),k(e,a),k(a,i),u=!0,g||($=q(e,"submit",D(r[4])),g=!0)},p(f,w){f[3]?p?p.p(f,w):(p=S(f),p.c(),p.m(s,null)):p&&(p.d(1),p=null);const P={};w&769&&(P.$$scope={dirty:w,ctx:f}),o.$set(P),(!u||w&2)&&(a.disabled=f[1]),w&2&&F(a,"btn-loading",f[1])},i(f){u||(v(o.$$.fragment,f),u=!0)},o(f){y(o.$$.fragment,f),u=!1},d(f){f&&b(e),p&&p.d(),z(o),g=!1,$()}}}function O(r){let e,t,s,l,n;return{c(){e=m("div"),e.innerHTML=`<div class="icon"><i class="ri-checkbox-circle-line"></i></div>
            <div class="content txt-bold"><p>Successfully changed the user email address.</p>
                <p>You can now sign in with your new email address.</p></div>`,t=h(),s=m("button"),s.textContent="Close",d(e,"class","alert alert-success"),d(s,"type","button"),d(s,"class","btn btn-secondary btn-block")},m(o,c){_(o,e,c),_(o,t,c),_(o,s,c),l||(n=q(s,"click",r[6]),l=!0)},p:E,i:E,o:E,d(o){o&&b(e),o&&b(t),o&&b(s),l=!1,n()}}}function S(r){let e,t,s;return{c(){e=C("to "),t=m("strong"),s=C(r[3]),d(t,"class","txt-nowrap")},m(l,n){_(l,e,n),_(l,t,n),k(t,s)},p(l,n){n&8&&I(s,l[3])},d(l){l&&b(e),l&&b(t)}}}function Q(r){let e,t,s,l,n,o,c,a;return{c(){e=m("label"),t=C("Password"),l=h(),n=m("input"),d(e,"for",s=r[8]),d(n,"type","password"),d(n,"id",o=r[8]),n.required=!0,n.autofocus=!0},m(i,u){_(i,e,u),k(e,t),_(i,l,u),_(i,n,u),H(n,r[0]),n.focus(),c||(a=q(n,"input",r[7]),c=!0)},p(i,u){u&256&&s!==(s=i[8])&&d(e,"for",s),u&256&&o!==(o=i[8])&&d(n,"id",o),u&1&&n.value!==i[0]&&H(n,i[0])},d(i){i&&b(e),i&&b(l),i&&b(n),c=!1,a()}}}function V(r){let e,t,s,l;const n=[O,K],o=[];function c(a,i){return a[2]?0:1}return e=c(r),t=o[e]=n[e](r),{c(){t.c(),s=U()},m(a,i){o[e].m(a,i),_(a,s,i),l=!0},p(a,i){let u=e;e=c(a),e===u?o[e].p(a,i):(W(),y(o[u],1,1,()=>{o[u]=null}),Y(),t=o[e],t?t.p(a,i):(t=o[e]=n[e](a),t.c()),v(t,1),t.m(s.parentNode,s))},i(a){l||(v(t),l=!0)},o(a){y(t),l=!1},d(a){o[e].d(a),a&&b(s)}}}function X(r){let e,t;return e=new N({props:{nobranding:!0,$$slots:{default:[V]},$$scope:{ctx:r}}}),{c(){T(e.$$.fragment)},m(s,l){L(e,s,l),t=!0},p(s,[l]){const n={};l&527&&(n.$$scope={dirty:l,ctx:s}),e.$set(n)},i(s){t||(v(e.$$.fragment,s),t=!0)},o(s){y(e.$$.fragment,s),t=!1},d(s){z(e,s)}}}function Z(r,e,t){let s,{params:l}=e,n="",o=!1,c=!1;async function a(){if(o)return;t(1,o=!0);const g=new j("../");try{await g.users.confirmEmailChange(l==null?void 0:l.token,n),t(2,c=!0)}catch($){A.errorResponseHandler($)}t(1,o=!1)}const i=()=>window.close();function u(){n=this.value,t(0,n)}return r.$$set=g=>{"params"in g&&t(5,l=g.params)},r.$$.update=()=>{r.$$.dirty&32&&t(3,s=R.getJWTPayload(l==null?void 0:l.token).newEmail||"")},[n,o,c,s,a,l,i,u]}class ee extends G{constructor(e){super(),J(this,e,Z,X,M,{params:5})}}export{ee as default};
