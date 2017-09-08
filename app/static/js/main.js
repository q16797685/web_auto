/**
 * Created by Donlink on 2017-08-15.
 */
"use strict";
(function () {
    angular
        .module('wangchengyang',[])
        .controller('wcy',['$scope','$q','$http',function($scope,$q,$http){
            function query(method,url,params,data){
                return $http({
                    method: method,
                    url: url,
                    data:data,
                    params: params,
                    contentType: 'application/json;charset=UTF-8',
                 
                })
            }

           /*主数据表格 */

            $scope.tableData = [
                {name:'搜索引擎接口',method:'POST',url:'http://172.17.200.94/login',data:[
                    {name:'username',value:3959},{name:'1',value:3959}
                ],response:null,resData:null,isChecked:false},

                {name:'测试',method:'GET',url:'emr/test/ds',data:[
                    {name:'fieldName',value:''},{name:'firstKey',value:''},{name:'secondKey',value:''},{name:'pageNo',value:1},{name:'pageSize',value:10}
                ],response:null,resData:null,isChecked:false},
            ];
           /*主数据表格 end*/

            //*点击运行按钮，触发事件*/
            $scope.run = function(){
                var listData = $scope.tableData;
                var listArr = [];
                var sendData = {};
                listData.forEach(function(v,i){
                    if(v.isChecked == true){
                        v.data.forEach(function(a,b){
							sendData[a.name] = a.value;
                        });
                        //listArr.push(query(v.method, v.url,sendData));
						if(v.method=="GET"){
							 query(v.method, v.url,sendData).then(function(resData){
                            //请求成功时
                            console.log('resData',resData)
                            v.response = resData.status;
							},function(errData){
                            //请求失败时
                            console.log('errData',errData);
                            v.response = errData.status;
							})
						}else if(v.method=="POST"){
							 query(v.method, v.url,'',sendData).then(function(resData){
                            //请求成功时
                            console.log('resData',resData)
                            v.response = resData.status;
							},function(errData){
                            //请求失败时
                            console.log('errData',errData);
                            v.response = errData.status;
							})
						}
                       

                    }
                });
                //$q.all(listArr).then(function(resData){
                //    console.log(resData)
                //})
            };
            //*增加 / 删除data*/
            $scope.delData = function(parentIndex,index){
                $scope.tableData[parentIndex].data.splice(index,1);
            };
            $scope.addData = function(parentIndex,index){
                $scope.tableData[parentIndex].data.push({name:'New',value:'value'});
            };
            //增加一个接口
            $scope.addQuery = function(){
                $scope.tableData.push(
                    {name:'新的接口',method:'GET',url:'172.17.200.94',data:[{name:'pageNo',value:1},{name:'pageSize',value:10}
                    ],response:null,resData:null,isChecked:false}
                );
            }

        }]);

})();