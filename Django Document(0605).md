# Django Document
> 2017.06.05 박현준

###  Django에서 모델의 특징
* 각각의 모델은 파이썬 클래스로 표현되며, django.db.models.Model 클래스의 서브클래스입니다.
* 모델 클래스의 어트리뷰트로 데이터베이스의 필드(컬럼)을 표현합니다.
* Django는 이러한 모델 클래스를 통해 데이터베이스 접근 API를 제공합니다.

#### Using model
* 모델은 정의한 후에는 INSTALLED_APPS 설정에 모델이 정의된 app을 추가해 주어야 합니다.

```
INSTALLED_APPS = (
    #...
    'myapp',
    #...
)
```

#### Fields
* 모델을 정의할 때 가장 중요한 부분은 바로 필드 선언입니다. 필드는 클래스 어트리뷰트로 표기됩니다

#### Field types
* 모델에 필드를 선언할때, 각각의 필드는 Field 클래스의 인스턴스여야합니다. 각 필드의 클래스 타입을 통해 Django는 아래와 같은 내용을 자동적으로 판단하여 동작할 수 있게 됩니다.

#### Field options
* 각각의 필드에 옵션을 줄수 있는데, 특정 필드에만 사용할 수 있는 옵션이 있습니다.

```
null
값이 True 이면, DB상의 해당 컬럼에 NULL 값을 할당할 수 있습니다. 즉, 데이터베이스의 NOT NULL 제약과 관련있는 옵션입니다.

blank
값이 True이면, 필드값을 입력하지 않아도 됩니다. 기본값은 False 입니다.

null 
null은 DB 상의 NOT NULL 제약과 연관된 옵션이라고 했을때, blank 옵션은 DB의 어떤 제약과도 관련이 없습니다. 
즉 blank 옵션을 설정한다고 해서 DB상에 어떤 제약이 걸리지는 않습니다. 다만, 유효성 검증(validation)과 연관이 있습니다. 
Django는 복잡한 구현없이 모델에 대한 HTML 폼을 쉽게 생성할 수 있도록 도와주는데, 이 폼 검증시에 blank 옵션이 False인 필드는 필수 입력 필드로 처리됩니다.

choices
enum과 같이 필드에 저장할 수 있는 값이 제한적인 경우에 사용할 수 있습니다. 옵션값은 아래와 같이 2중 튜플(또는 리스트)로 설정해야합니다. 
``` 

#### Automatic primary key fields
```
id = models.AutoField(primary_key=True)
```

* 위의 필드는 자동증가(auto increment)하는 primary key 필드입니다.
* 직접 primary key 필드를 선언하고 싶다면, 모델의 필드 중 하나에 "primary_key=True" 옵션을 주면 됩니다. Django는 모델에 primary_key=True 옵션이 명시적으로 선언된 필드가 있다면 자동적으로 id 필드를 생성하지 않습니다.
* Django의 모델은 필수적으로 하나의 Primary Key 필드를 가져야 합니다. 다시 말해서, 직접 선언했던 자동으로 생성되었던지 관계없이 1개의 primary key 필드를 가져야 합니다.

#### Verbose field names
* verbose name을 지정할 때는 관습적으로 첫글자를 대문자화하지 않고 소문자로 지정합니다. Django가 필요한 경우 알아서 대문자화하여 표시하기 때문입니다.

#### Relationships
* RDBMS 테이블간에 관계를 정의하고, 그 관계를 기반으로 쿼리나 DB의 무결성을 보장할 수 있게 해줍니다.

#### Many-to-one relationships
* 일대다 관계를 정의하려면 django.db.models.ForeignKey 클래스를 이용하여 필드를 선언하면 됩니다. ForeignKey 필드 선언시에 관계를 맺을 모델 클래스를 인자로 넘겨주어야 합니다.

#### Many-to-many relationships
* 다대다 관계를 선언할때는 ManyToManyField를 사용합니다. ForeignKey 필드와 마찬가지로 관계를 가지는 모델 클래스를 첫번째 인자로 받습니다.

#### one-to-one relationships
* 일대일 관계를 정의하려면, OneToOneField를 이용하면 됩니다. 다른 관계 필드와 마찬가지로 모델 클래스의 어트리뷰트로 선언하면 됩니다.

#### Models across files
* 른 앱에 선언된 모델과 관계를 가질 수 있습니다. 그렇게 하려면, 다른 앱의 모델을 import 해서 아래와 같이 관계 필드를 선언하면 됩니다.

#### Field name restrictions
* Django는 모델 필드이름에 2가지 제약을 두고 있습니다. 파이썬 예약어는 필드이름으로 사용할 수 없습니다. 이 경우 파이썬 문법에러가 발생됩니다.

#### Custom field types
* Django에서 제공하는 필드 타입들 중에 당신의 목적에 적합한 타입이 없거나 특정 데이터베이스에서만 제공하는 특별한 타입을 사용하고 싶다면, 필드를 직접 만들어 사용할 수도 있습니다.