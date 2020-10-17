X_train, X_test, y_train, y_test = train_test_split(iris.drop('species',axis=1),
iris['species'], stratify=iris['species'], test_size=0.30)