# 2 Neo4j CQL

## CQL简介

CQL代表Cypher查询语言。 像Oracle数据库具有查询语言SQL，Neo4j具有CQL作为查询语言。



**Neo4j CQL -**

- 它是Neo4j图形数据库的查询语言。
- 它是一种声明性模式匹配语言
- 它遵循SQL语法。
- 它的语法是非常简单且人性化、可读的格式。

**如Oracle SQL -**

- Neo4j CQL 已命令来执行数据库操作。
- Neo4j CQL 支持多个子句像在哪里，顺序等，以非常简单的方式编写非常复杂的查询。
- NNeo4j CQL 支持一些功能，如字符串，Aggregation.In 加入他们，它还支持一些关系功能。

### Neo4j CQL命令/条款

常用的Neo4j CQL命令/条款如下：

| S.No. | CQL命令/条      | 用法                         |
| ----- | --------------- | ---------------------------- |
| 1。   | CREATE 创建     | 创建节点，关系和属性         |
| 2。   | MATCH 匹配      | 检索有关节点，关系和属性数据 |
| 3。   | RETURN 返回     | 返回查询结果                 |
| 4。   | WHERE 哪里      | 提供条件过滤检索数据         |
| 5。   | DELETE 删除     | 删除节点和关系               |
| 6。   | REMOVE 移除     | 删除节点和关系的属性         |
| 7。   | ORDER BY以…排序 | 排序检索数据                 |
| 8。   | SET 组          | 添加或更新标签               |

  

### Neo4j CQL 函数

以下是常用的Neo4j CQL函数：

| S.No. | 定制列表功能      | 用法                                             |
| ----- | ----------------- | ------------------------------------------------ |
| 1。   | String 字符串     | 它们用于使用String字面量。                       |
| 2。   | Aggregation 聚合  | 它们用于对CQL查询结果执行一些聚合操作。          |
| 3。   | Relationship 关系 | 他们用于获取关系的细节，如startnode，endnode等。 |

我们将在后面的章节中详细讨论所有Neo4j CQL命令，子句和函数语法，用法和示例。

### Neo4j CQL数据类型

这些数据类型与Java语言类似。 它们用于定义节点或关系的属性
Neo4j CQL支持以下数据类型：

| S.No. | CQL数据类型 | 用法                            |
| ----- | ----------- | ------------------------------- |
| 1.    | boolean     | 用于表示布尔文字：true，false。 |
| 2.    | byte        | 用于表示8位整数。               |
| 3.    | short       | 用于表示16位整数。              |
| 4.    | int         | 用于表示32位整数。              |
| 5.    | long        | 用于表示64位整数。              |
| 6.    | float       | I用于表示32位浮点数。           |
| 7.    | double      | 用于表示64位浮点数。            |
| 8.    | char        | 用于表示16位字符。              |
| 9.    | String      | 用于表示字符串。                |



### 2.1 CREATE

Neo4j使用CQL“CREATE”命令

- 创建没有属性的节点
- 使用属性创建节点
- 在没有属性的节点之间创建关系
- 使用属性创建节点之间的关系
- 为节点或关系创建单个或多个标签

#### CQL创建一个没有属性的节点

```
CREATE (<node-name>:<label-name>)
```

语法说明

| 语法元素      | 描述                       |
| ------------- | -------------------------- |
| CREATE        | 它是一个Neo4j CQL命令。    |
| \<node-name>  | 它是我们要创建的节点名称。 |
| \<label-name> | 它是一个节点标签名称       |

```
例子：
创建一个简单的“Employee”节点
CREATE (emp:Employee)
这里 emp 是一个节点名
Employee 是 emp 节点的标签名称
```

#### Neo4j CQL创建具有属性的节点

Neo4j CQL“CREATE”命令用于创建带有属性的节点。 它创建一个具有一些属性（键值对）的节点来存储数据。

```
CREATE (
   <node-name>:<label-name>
   { 	
      <Property1-name>:<Property1-Value>
      ........
      <Propertyn-name>:<Propertyn-Value>
   }
)
```

```
例子：
创建
CREATE (dept:Dept { deptno:10,dname:"Accounting",location:"Hyderabad" })

创建具有一些属性（id，name，sal，deptno）的Employee节点
CREATE (emp:Employee{id:123,name:"Lokesh",sal:35000,deptno:10})

```

### 2.2 MATCH  | RETURN

Neo4j CQL MATCH命令用于 

- 从数据库获取有关节点和属性的数据
- 从数据库获取有关节点，关系和属性的数据

 ```
MATCH 
(
   <node-name>:<label-name>
)
 ```

语法说明

| 语法元素      | 描述                         |
| ------------- | ---------------------------- |
| \<node-name>  | 这是我们要创建一个节点名称。 |
| \<label-name> | 这是一个节点的标签名称       |

**注意-**我们不能单独使用MATCH 从数据库检索数据。 如果我们单独使用它，那么我们将InvalidSyntax错误。

```
！错误例子！ 
#单独使用MATCH命令从数据库检索数据会发生什么
#dept是节点名称
#Dept是emp节点的标签名称

MATCH (dept:Dept)
-->must be RETURN or update

```

Neo4j CQL RETURN子句用于 

- 检索节点的某些属性
- 检索节点的所有属性
- 检索节点和关联关系的某些属性
- 检索节点和关联关系的所有属性

```
RETURN 
   <node-name>.<property1-name>,
   ........
   <node-name>.<propertyn-name>
```

语法说明:

| 语法元素             | 描述                                                         |
| -------------------- | ------------------------------------------------------------ |
| \<node-name>         | 它是我们将要创建的节点名称。                                 |
| \<Property1-name>... | 属性是键值对。 \<Property-name>定义要分配给创建节点的属性的名称 |

```
续上错误例子
如果单独使用RETURN命令从数据库检索数据

RETURN dept.deptno
不能单独使用RETURN子句
```

#### MATCH + RETURN

在Neo4j CQL中，我们不能单独使用MATCH或RETURN命令，因此我们应该合并这两个命令以从数据库检索数据。

Neo4j使用CQL MATCH + RETURN命令 

- 检索节点的某些属性
- 检索节点的所有属性
- 检索节点和关联关系的某些属性
- 检索节点和关联关系的所有属性

```
MATCH Command
RETURN Command
```

```
例子
检索Dept节点的一些属性（deptno，dname）数据

MATCH (dept: Dept)
RETURN dept.deptno, dept.dname

dept是节点名称
这里Dept是一个节点标签名
deptno是dept节点的属性名称
dname是dept节点的属性名

MATCH (dept: Dept)
RETURN dept.deptno,dept.dname,dept.location

MATCH (dept: Dept)
RETURN dept
```

### 2.3 关系相关基础

基于方向性，Neo4j关系被分为两种主要类型。

- 单向关系
- 双向关系

在以下场景中，我们可以使用Neo4j CQL CREATE命令来创建两个节点之间的关系。 这些情况适用于Uni和双向关系。

- 在两个现有节点之间创建无属性的关系
- 在两个现有节点之间创建与属性的关系
- 在两个新节点之间创建无属性的关系
- 在两个新节点之间创建与属性的关系
- 在具有WHERE子句的两个退出节点之间创建/不使用属性的关系

**→**

每个关系（→）包含两个节点

- 从节点
- 到节点

对于节点，它们是两种关系

- 外向关系
- 传入关系

### CREATE 创建标签

Label是Neo4j数据库中的节点或关系的名称或标识符。

我们可以将此标签名称称为关系为“关系类型”。

我们可以使用CQL CREATE命令为节点或关系创建单个标签，并为节点创建多个标签。

**单个标签到节点**

语法：

```
CREATE (<node-name>:<label-name>)
```

| S.No. | 语法元素                | 描述                      |
| ----- | ----------------------- | ------------------------- |
| 1     | CREATE 创建             | 它是一个Neo4j CQL关键字。 |
| 2     | \<node-name> <节点名称> | 它是一个节点的名称。      |
| 3     | \<label-name><标签名称> | 这是一个节点的标签名称。  |

```
例子：
如何使用属性和这两个节点之间的关系创建两个节点。

注-我们将创建两个节点：客户节点 (Customer) 和信用卡节点 (CreditCard)。
客户节点包含：ID，姓名，出生日期属性
CreditCard节点包含：id，number，cvv，expiredate属性
客户与信用卡关系：DO_SHOPPING_WITH
CreditCard到客户关系：ASSOCIATED_WITH

1、创建客户节点
CREATE (e:Customer{id:"1001",name:"Abc",dob:"01/10/1982"})

2、创建CreditCard节点
CREATE (cc:CreditCard
{id:"5001",number:"1234567890",
cvv:"888",expiredate:"20/17"})

3、观察节点
现在我们创建了两个节点：Customer和CreditCard
我们需要使用带有RETURN子句的Neo4j CQL MATCH命令查看这两个节点的详细信息
MATCH (e:Customer)
RETURN e.id,e.name,e.dob

MATCH (cc:CreditCard)
RETURN cc.id,cc.number,cc.cvv,cc.expiredate

```



